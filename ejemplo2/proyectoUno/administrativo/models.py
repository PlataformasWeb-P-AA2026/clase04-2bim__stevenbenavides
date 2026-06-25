from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)
    
    def get_numeros_telefonicos(self):
        return len(self.numeros_telefonicos.all())
    
    def mostar_operadora(self):
        tipo = "Coonvencional"
        if self.telefono.starts_with(099)
            tipo = "Claro"
        elif self.telefono.starts_with(098)
            tipo = "movistar"

        return self.telefono.all()
    

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)

    
