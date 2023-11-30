from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    propietario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f'Cita para {self.mascota.nombre} el {self.fecha}'
