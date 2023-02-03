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
    availabel = models.IntegerField(default=100)
    def __str__(self):
        return self.user.username + ' ' + str(self.name)
    
    def make_booking(self, user, ticket_quantity):
        if ticket_quantity > self.availabel or ticket_quantity < 1:
            return None
        booking = Booking.objects.create(user=user, ticket=self, ticket_quantity=ticket_quantity)
        booking.save()
        self.availabel -= ticket_quantity
        self.save()
        return booking
    
    def cancel_booking(self, booking):
        try:
            self.availabel += booking.ticket_quantity
            self.save()
            booking.delete()
            return True
        except:
            return False

class Booking(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=None)
    ticket_quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.user.username + ' ' + str(self.ticket_quantity)
