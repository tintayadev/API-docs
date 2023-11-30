from rest_framework import serializers
from .models import Mascota, Cita

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


class CitaSerializer(serializers.ModelSerializer):
    mascota = MascotaSerializer()

    class Meta:
        model = Cita
        fields = '__all__'

    def create(self, validated_data):
        mascota_data = validated_data.pop('mascota')
        mascota_instance = Mascota.objects.create(**mascota_data)
        
        cita_instance = Cita.objects.create(mascota=mascota_instance, **validated_data)
        return cita_instance