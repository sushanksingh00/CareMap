# CareMap

Note: Project now uses Django for the web backend. The original Flask implementation is preserved under `flask_app/`.

Quick start (Django):

1. Create/activate a virtualenv and install deps:

	- `pip install -r requirements.txt`

2. Run database migrations:

	- `python manage.py migrate`

3. Start the dev server:

	- `python manage.py runserver`

App will be available at http://127.0.0.1:8000/.

Flask version (preserved):

- Code: `flask_app/`
- Requirements: `flask_app/requirements.txt`
- Original entry file: `flask_app/app.py`

#### Video Demo: https://www.youtube.com/watch?v=kwQX0F6eih4

### Screenshots

![Homepage](./Screenshot%202025-12-24%20at%2010.00.53%E2%80%AFPM.png)
![Chat View](./Screenshot%202025-12-24%20at%2010.01.20%E2%80%AFPM.png)
![History Page](./Screenshot%202025-12-24%20at%2010.01.32%E2%80%AFPM.png)

#### Description:

**CareMap** is a web-based health assistant that helps users understand potential medical conditions based on symptoms they enter. It was developed as my final project for CS50x, with the goal of giving people a simple, accessible tool to check their health concerns from home.

We often ignore small symptoms, or panic over things that turn out to be minor. CareMap tries to reduce both confusion and unnecessary stress. By simply entering symptoms like “headache,” “chest pain,” or “tiredness,” users can get a list of possible medical conditions that match what they’re feeling. The app uses the Gemini API to intelligently generate these suggestions. It’s not meant to replace a doctor, but it helps people get an early idea of whether something might need attention.

### How it Works

When a user visits the site, they’re greeted with a login/register option. Once authenticated, they can enter one or more symptoms into a form. When the form is submitted, the backend sends those symptoms to the Gemini API, which processes the input and returns possible matching conditions. These results are then displayed directly below, along with some basic information that can guide the user’s next steps.

Each user's search history is stored in a database, so they can log in later and revisit past results. This is useful for tracking recurring issues or showing a doctor what symptoms were experienced and when.

I designed CareMap to handle both mild and serious situations. For example, if someone enters “sore throat,” the suggestions might include minor issues like a cold or allergies. But entering “chest pain” might return more serious risks like a heart condition. This contrast is intentional — I wanted the app to be equally useful for daily health questions and early warnings about critical problems.

### Technologies Used

The backend is written in **Python using Flask**, which handles routing, session management, form processing, and API interaction. For the database, I used **SQLite**, which stores user credentials and symptom history. On the frontend, I used **HTML, CSS, and vanilla JavaScript** to keep the UI simple and responsive.

The integration with **Gemini API** is the heart of the project. It takes a string of symptoms as input and returns a medical response based on Gemini’s intelligent language model. I chose Gemini because it’s flexible, fast, and capable of handling vague or mixed symptom descriptions.

The project folder contains the following files:

- `app.py` – Main Flask application with all backend logic: routes for login, register, logout, form submission, and history display.
- `templates/` – Folder containing HTML templates (`login.html`, `register.html`, `index.html`, etc.).
- `static/` – Contains CSS and JS files for styling and basic interactivity.
- `schema.sql` – SQL schema for setting up the database.
- `helpers.py` – Contains helper functions like password hashing, login checks, and database queries.
- `README.md` – This file, which explains the entire project.
- `history.db` – SQLite database containing user accounts and saved search results.

### Design Decisions

One of the key decisions was to keep the interface minimal. I wanted it to feel like a lightweight assistant — no clutter, just input and output. Users don’t need medical knowledge to use the app. They just type what they feel, and the app tries to help.

I also debated between using a large pre-built medical database versus relying on an AI API. I chose Gemini because it allows more flexible, natural symptom input, rather than exact keyword matches. This makes the experience feel more human and conversational.

Security was important as well. Passwords are hashed before storing, and session handling ensures users can't access data that isn’t theirs. I didn’t implement email verification due to time constraints, but that could be added later.

### Future Improvements

I plan to add a **Profile** tab, where users can edit their name, contact info, and view an extended medical history chart. I also want to add a **Nearby Doctors** feature, which recommends medical professionals in the user’s city based on the symptoms entered. This would involve integrating Google Maps API or similar services.

Another possible upgrade is allowing users to enter symptoms via voice input, and receiving spoken responses. This would make CareMap even more accessible to users with limited literacy or tech experience.

---

CareMap is more than just a class project to me. It’s something I built to solve a real problem — the gap between worrying about health and knowing what steps to take. Through CS50, I learned how to go from an idea to a working product that could genuinely help people. I’m proud of what I’ve built and excited to keep improving it.
