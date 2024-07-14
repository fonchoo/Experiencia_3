from rest_framework import serializers
from .models import Produc

class ProducSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produc
        fields = '__all__'