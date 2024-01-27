from rest_framework import permissions
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import Reservation
from .forms import ReservationForm

class BookingsCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            form_data = self.request.data 
            form = ReservationForm(form_data)
            if form.is_valid():
                reservation_instance = form.save()

                # Prepare the email body with all reservation details
                email_body = f'''
                    A new reservation has been made:

                    Name: {reservation_instance.name}
                    Phone: {reservation_instance.phone}
                    Email: {reservation_instance.email}
                    Date: {reservation_instance.date}
                    Time: {reservation_instance.time}
                    Guests: {reservation_instance.guests}
                    Message: {reservation_instance.message}
                '''

                # Send an email to the admin with all reservation details
                send_mail(
                    'New Reservation',
                    email_body,
                    'indrajeetsinghyadav4@gmail.com',  
                    ['indrajeetsinghyadav4@gmail.com'],  
                    fail_silently=False,
                )
                
                return Response({'success': 'Table booked successfully'})
        except Exception as e:
            return Response({'error': f'Failed to book the table. Error: {str(e)}'})
