from rest_framework import generics

from django.contrib.auth.models import User
from .serializers import RegistrationSerializer




class Registration(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    