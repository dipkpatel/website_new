from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    """
    A reservation created by a user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    

class ReservationDate(models.Model):
    """
    A date under reservation.
    """
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    # This is better as a DateField, but having it as a CharField makes it
    # ready to plug into the calendar.
    date = models.CharField(max_length=16)
