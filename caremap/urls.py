from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('chat', views.chat_view, name='chat'),
    path('history', views.history_view, name='history'),
    path('history/<int:pk>', views.history_detail_view, name='history_detail'),
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('models', views.list_models_view, name='models'),
    path('profile', views.profile, name='profile'),
]
