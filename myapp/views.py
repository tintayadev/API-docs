from rest_framework import generics
from .models import Mascota, Cita
from .serializers import MascotaSerializer, CitaSerializer

class MascotaListCreateView(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class MascotaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class CitaListCreateView(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer