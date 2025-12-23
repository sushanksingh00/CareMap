import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest, HttpResponse

from .models import DiagnosisHistory, UserProfile

# External libs used by Flask version
import markdown as md
import google.generativeai as genai

MODEL_NAME = "gemini-2.5-flash"


def apology(request: HttpRequest, message: str, code: int = 400) -> HttpResponse:
    return render(request, 'apology.html', {'top': code, 'bottom': message}, status=code)


def index(request: HttpRequest) -> HttpResponse:
    profile_photo_url = None
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        if profile and getattr(profile, 'profile_photo_url', ''):
            profile_photo_url = profile.profile_photo_url

    return render(request, 'homepage.html', {
        'profile_photo_url': profile_photo_url,
    })


@require_http_methods(["GET", "POST"])
def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'apology.html', {'top': 400, 'bottom': 'Must provide Username and Password'}, status=400)

        if User.objects.filter(username=username).exists():
            return render(request, 'apology.html', {'top': 400, 'bottom': 'Username Taken'}, status=400)

        user = User.objects.create_user(username=username, email=email or '', password=password)
        user.save()
        return redirect('login')

    return render(request, 'registration.html')


@require_http_methods(["GET", "POST"])
def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'apology.html', {'top': 403, 'bottom': 'must provide username and password'}, status=403)

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'apology.html', {'top': 403, 'bottom': 'invalid username and/or password'}, status=403)

        login(request, user)
        return redirect('index')

    return render(request, 'login.html')


@login_required
@require_http_methods(["GET", "POST"])
def chat_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        symptoms = request.POST.get('symptoms')

        if not name or not age or not symptoms:
            return render(request, 'apology.html', {'top': 403, 'bottom': 'must provide name, age, and symptoms'}, status=403)

        api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('GENAI_API_KEY')
        api_key = "AIzaSyB2my6BPN59Wm7nHsJm8SKt2705lnxUKZg"

        if not api_key:
            return render(request, 'apology.html', {'top': 500, 'bottom': 'Google API key missing. Set GOOGLE_API_KEY.'}, status=500)

        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(MODEL_NAME)
            chat = model.start_chat(
                history=[
                    {"role": "user", "parts": ["I need your help"]},
                    {"role": "model", "parts": ["What help do you need?"]},
                ]
            )

            prompt = (
                """Act as a medical assistant. Please analyze the following symptoms and provide:
            1. A summary of possible causes.
            2. A classification of severity (mild/moderate/severe).
            3. Advice on whether to seek medical attention.
            4. Output formatted clearly using headings and bullet points.

            Symptoms: {symptoms}
            given the age of the pateint : {age}
            """.format(symptoms=symptoms, age=age)
            )

            response = chat.send_message(prompt, stream=True)
            diagnosis_text_raw = "".join(chunk.text for chunk in response).strip()
            diagnosis_html = md.markdown(diagnosis_text_raw)

            DiagnosisHistory.objects.create(
                user=request.user,
                name=name,
                age=int(age),
                symptoms=symptoms,
                diagnosis=diagnosis_text_raw,
            )

            return render(request, 'result.html', {"symp": diagnosis_html})
        except Exception as e:
            print(e)
            return render(request, 'apology.html', {'top': 500, 'bottom': 'An error occurred. Please try again.'}, status=500)
    # GET: Pre-fill name and age from profile if available
    profile = getattr(request.user, 'profile', None)
    initial_name = getattr(profile, 'name', '') if profile else ''
    initial_age = getattr(profile, 'age', '') if profile and profile.age is not None else ''

    return render(request, 'chatbox.html', {
        'initial_name': initial_name,
        'initial_age': initial_age,
    })


@login_required
def history_view(request: HttpRequest) -> HttpResponse:
    records = list(
        DiagnosisHistory.objects.filter(user=request.user)
        .values('id', 'name', 'age', 'symptoms', 'timestamp')
    )
    return render(request, 'history.html', {'records': records})


def aboutus_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'aboutus.html')


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('index')


@login_required
def list_models_view(request: HttpRequest) -> HttpResponse:
    api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('GENAI_API_KEY')
    if not api_key:
        return apology(request, 'Google API key missing. Set GOOGLE_API_KEY.', 500)

    try:
        genai.configure(api_key=api_key)
        models = genai.list_models()
        items = []
        for m in models:
            methods = list(getattr(m, 'supported_generation_methods', []))
            items.append({
                'name': getattr(m, 'name', ''),
                'methods': methods,
            })
        return render(request, 'models.html', {'models': items})
    except Exception as e:
        print(e)
        return apology(request, 'Failed to list models. Check API key/permissions.', 500)


@login_required
def history_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    obj = get_object_or_404(DiagnosisHistory, pk=pk, user=request.user)
    diagnosis_html = md.markdown(obj.diagnosis or "")
    return render(request, 'diagnosis_detail.html', { 'diagnosis': diagnosis_html })


@login_required
@require_http_methods(["GET", "POST"])
def profile(request: HttpRequest) -> HttpResponse:
    """Create/update and display the current user's profile.

    - GET: Show existing profile (or empty form if none exists)
    - POST: Create or update profile from submitted form fields
    """

    profile = getattr(request.user, 'profile', None)
    saved = False

    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        email = (request.POST.get('email') or '').strip()
        phone_number = (request.POST.get('phone_number') or '').strip()
        city = (request.POST.get('city') or '').strip()
        country = (request.POST.get('country') or '').strip()
        profile_photo_url = (request.POST.get('profile_photo_url') or '').strip()
        age_raw = (request.POST.get('age') or '').strip()

        age_val = None
        if age_raw:
            try:
                age_val = int(age_raw)
            except ValueError:
                age_val = None

        if profile is None:
            profile = UserProfile(user=request.user)

        profile.name = name
        profile.email = email
        profile.phone_number = phone_number
        profile.city = city
        profile.country = country
        profile.profile_photo_url = profile_photo_url
        profile.age = age_val

        profile.save()
        saved = True

    context = {
        'profile': profile,
        'saved': saved,
    }
    return render(request, 'profile.html', context)

