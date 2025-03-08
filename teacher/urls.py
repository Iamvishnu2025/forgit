# ✅ Correct: dapp/urls.py should only contain app-specific routes
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", login, name="login"),
    path('login/', admin_login, name='admin_login'),
  
]
