from django.db import models


# Create your models here.

class Article(models.Model):  # con models.Model le indico que esta clase es un modelo de BBDD
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default="null", verbose_name='Imagen', upload_to="articles")
    public = models.BooleanField(verbose_name='¿Publicado?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        if self.public:
            publico = 'Publicado'
        else:
            publico = 'Privado'
        return f"{self.title} - {publico} ({self.id})"


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'