from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    """
    A reservation created by a user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.account) + " " + str(start_date) + " " + str(end_date)
