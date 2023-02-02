from django.db import models
from django.contrib.auth.models import User
import datetime

class Ticket(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default="No description")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    size = models.IntegerField(default=100)

    def __str__(self):
        return self.user.username + ' ' + str(self.name)

class Booking(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=None)
    ticket_quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.user.username + ' ' + str(self.ticket_quantity)
