from django.db import models

# Create your models here.

class Publicacion(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'publicacion' #nombre de la tabla en la BD
        verbose_name = 'Publicacion' #nombre de la tabla en un panel de administración de django
        ordering = ["title"]


class Noticia(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publicacion)

    class Meta:
        db_table = 'noticia' #nombre de la tabla en la BD
        verbose_name = 'Noticia' #nombre de la tabla en un panel de administración de django
        ordering = ["headline"]

    def __str__(self):
        return self.headline