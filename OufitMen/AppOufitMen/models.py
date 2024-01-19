from django.db import models

class Producto(models.Model):
    prod_Id=models.AutoField(primary_key=True, verbose_name="ID del producto")
    prod_Nombre = models.CharField(max_length=255)
    prod_Descripcion = models.TextField()
    prod_Precio = models.DecimalField(max_digits=10, decimal_places=2)
    prod_Talla = models.CharField(max_length=10)
    prod_Color = models.CharField(max_length=50)
    prod_Imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
