from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Stock(models.Model): #stock

    nombre = models.CharField(max_length=40)

    cantidad = models.IntegerField()

 

class Cliente(models.Model): #cliente

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) #CASCADE HACE QUE CADA VEZ QUE UN USER SEA ELIMINADO SEA ELIMINADO DE CLIENTE
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    item = models.CharField(max_length=140, default='SOME STRING')
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
 

class Distribuidora(models.Model): #distribuidora

    nombre = models.CharField(max_length=30)

    apellido = models.CharField(max_length=30)

    email = models.EmailField()

    profesion = models.CharField(max_length=30)

 
class Local(models.Model): #distribuidora

    nombre = models.CharField(max_length=30)

    calle = models.CharField(max_length=30)

    país = models.CharField(max_length=30)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null= True,  blank=True)

class Tag(models.Model):
    nombre = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    CATEGORY = (
        ('Pulsera', 'Pulsera'),
        ('Collar', 'Collar'),
        ('Pendiente', 'Pendiente'),
        ('Pañuelo', 'Pañuelo'),
        )
    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField(max_length=8, null=True)
    categoria = models.CharField(max_length=200, null=True, choices=CATEGORY)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)           
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.nombre


class Ordenar(models.Model):
    STATUS = (
        ('Pendiente','Pendiente'),
        ('No se puede entregar','No se puede entregar'),
        ('Entreado','Entregado'),
    )
    cliente = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL) #CADA VEZ QUE EL CLIENTE DE BAJA AL PEDIDO NO SE BORRE DE LA BASE DE DATOS
    producto = models.ForeignKey(Producto, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(Producto, auto_now_add=True, null=True)
    estado = models.CharField(max_length=200, null=True, choices=STATUS)
    def __str__(self):
        return self.producto.nombre
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'
# Create your models here.

