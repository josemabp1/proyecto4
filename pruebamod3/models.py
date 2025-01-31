from django.db import models

# Create your models here.
class Lugar(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"
    
    class Meta:
        db_table = 'lugar' #nombre de la tabla en la BD
        verbose_name = 'Lugar' #nombre de la tabla en un panel de administración de django
        ordering = ["name"]


class Restaurante(models.Model):
    lugar = models.OneToOneField(
        Lugar,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.lugar.name

    class Meta:
        db_table = 'restaurante' #nombre de la tabla en la BD
        verbose_name = 'Restaurante' #nombre de la tabla en un panel de administración de django
        ordering = ["lugar"]


class Camarero(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurante)
    
    class Meta:
        db_table = 'camarero' #nombre de la tabla en la BD
        verbose_name = 'Camarero' #nombre de la tabla en un panel de administración de django
        ordering = ["name"]