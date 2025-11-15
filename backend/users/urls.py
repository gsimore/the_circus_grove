from django.urls import path
from .views import UserRegistrationView, UserDetailView, UserListView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('', UserListView.as_view(), name='list'),
]
