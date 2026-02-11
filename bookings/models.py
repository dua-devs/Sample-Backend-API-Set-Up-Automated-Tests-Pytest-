from django.db import models

class Booking(models.Model):
    user_id = models.IntegerField()
    flight_id = models.IntegerField()
    seats = models.IntegerField()
    travel_date = models.DateField()
    status = models.CharField(max_length=20, default="CONFIRMED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - User {self.user_id}"
