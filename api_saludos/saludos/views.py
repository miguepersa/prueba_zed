from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Saludo
from .serializers import SaludoSerializer

# Create your views here.
class SaludoViewset(ModelViewSet):
    serializer_class = SaludoSerializer
    queryset = Saludo.objects.all()
