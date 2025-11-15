from django.urls import path
from .views import CheckInListCreateView, CheckInDetailView

app_name = 'checkins'

urlpatterns = [
    path('', CheckInListCreateView.as_view(), name='checkin-list'),
    path('<int:pk>/', CheckInDetailView.as_view(), name='checkin-detail'),
]
