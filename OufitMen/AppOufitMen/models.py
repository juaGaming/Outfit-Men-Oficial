from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Usuario(AbstractBaseUser):
    Usu_Documento = models.BigIntegerField(verbose_name="N° Documento", primary_key=True)
    Usu_Nombre = models.TextField(max_length=40)
    Usu_Apellido = models.TextField(max_length=40)
    Usu_Correo = models.EmailField(max_length=50, unique=True, verbose_name="Correo Electronico")
    #USERNAME_FIELD = 'Usu_Documento'
    USERNAME_FIELD = 'Usu_Documento'
    
class Categoria_producto(models.Model):
    Id_Categoria=models.AutoField(verbose_name="id categoria",primary_key=True)
    Nombre=models.TextField(max_length= 40)
    Descripcion=models.TextField(max_length=250)


class Producto(models.Model):
    prod_Id=models.AutoField(primary_key=True, verbose_name="ID del producto")
    prod_Nombre = models.CharField(max_length=255)
    prod_Descripcion = models.TextField()
    prod_Precio = models.DecimalField(max_digits=10, decimal_places=2)
    prod_Talla = models.CharField(max_length=10)
    prod_Color = models.CharField(max_length=50)
    prod_Imagen = models.ImageField(upload_to='productos/', null=True, blank=True)


     

class CarritoCompra(models.Model):
    Car_Id = models.AutoField(verbose_name="ID carro de compras", primary_key=True)
    Car_Id_Producto = models.ForeignKey(Producto, verbose_name="ID Producto", on_delete=models.CASCADE)
    Car_Id_Usuario = models.ForeignKey(Usuario, verbose_name="ID Usuario", on_delete=models.CASCADE)
    Car_Estado = models.TextField(max_length=30)
    
    
    
    
                 
class Pedido(models.Model):
    Pd_Id=models.AutoField(verbose_name="ID del Pedido",primary_key=True)
    Pd_Id_Usuario=models.BigIntegerField(verbose_name="ID del Usuario")
    Pd_Fecha_envio=models.DateTimeField()


class DetallePedido(models.Model):
    Detap_Id = models.AutoField(verbose_name="ID Detalle pedido", primary_key=True)
    Deta_Id_Pedido = models.ForeignKey(Pedido, verbose_name="ID Pedido", on_delete=models.CASCADE)
    Detap_Id_Usuario = models.ForeignKey(Usuario, verbose_name="ID Usuario", on_delete=models.CASCADE)
    Detap_Fecha_Envio = models.DateTimeField()
    Detap_Direccion = models.TextField(max_length=40)
    Detap_Estado_Envio = models.TextField(max_length=50)
    
     
class Envio_Producto(models.Model):
    Env_Id=models.AutoField(verbose_name="ID del envios",primary_key=True)
    Env_Id_Producto=models.ForeignKey(Producto,verbose_name="ID del Producto", on_delete=models.CASCADE)
    Env_Id_usuario=models.ForeignKey
    Env_Fecha_hora=models.DateTimeField() 
     
     
class Metodo_pago(models.Model):
    Mp_Id=models.AutoField(verbose_name="ID  de pago",primary_key=True)
    Mp_Pedido=models.ForeignKey(Pedido,verbose_name="ID pedido",on_delete=models.CASCADE)
    Mp_Metodo=models.TextField(max_length=40)
    Mp_Pago=models.IntegerField()
     
      
     
class Comentarios(models.Model):
    Ct_Id = models.AutoField(verbose_name="ID Comentario", primary_key=True)
    Ct_Id_Usu = models.ForeignKey(Usuario, verbose_name="ID Usuario", on_delete=models.CASCADE)
    Ct_Id_Prod = models.ForeignKey(Producto, verbose_name="ID Producto", on_delete=models.CASCADE)
    Ct = models.TextField(max_length=250)
    Ct_Cali = models.IntegerField()