from django.urls import path, include
from accounts.views import ProfileView, UserLogin
from .views import HomeView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', UserLogin.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
]
