from django.urls import path
from .views import bookings_view, availability_view

urlpatterns = [
    path("bookings/", bookings_view),
    path("availability/", availability_view),
]
