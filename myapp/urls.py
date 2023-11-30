from django.urls import path
from .views import MascotaListCreateView, MascotaDetailView, CitaListCreateView, CitaDetailView

urlpatterns = [
    path('mascotas/', MascotaListCreateView.as_view(), name='mascota-list-create'),
    path('mascotas/<int:pk>/', MascotaDetailView.as_view(), name='mascota-detail'),
    path('citas/', CitaListCreateView.as_view(), name='cita-list-create'),
    path('citas/<int:pk>/', CitaDetailView.as_view(), name='cita-detail'),
]
