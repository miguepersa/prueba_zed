from rest_framework import serializers
from .models import Saludo


class SaludoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saludo
        fields = '__all__'
