from django.urls import path
from booking.views import ticket_list, make_booking, booking_confirmation
from . import views

urlpatterns = [
    path('', ticket_list, name='ticket_list'),
    path('booking/<int:ticket_id>/', make_booking, name='make_booking'),
    path('booking/confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
    path('signup/', views.signup, name='signup'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
]
