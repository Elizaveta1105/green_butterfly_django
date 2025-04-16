from django.urls import path
from . import views
from . import apps
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

app_name = apps.AppAuthConfig.name

urlpatterns = [
    path('signup', views.SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(template_name="app_auth/login.html", form_class=LoginForm, redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(template_name="app_auth/logout.html"), name="logout")
]