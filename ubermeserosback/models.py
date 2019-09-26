from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_lenght=40)
    apellido = models.CharField(max_lenght=40)
    email = models.CharField(max_lenght=40)
    telefono = models.IntegerField()
    contrasena = models.CharField(max_lenght=40)
    avatar = models.ImageField(max_lenght=40)
    activo = models.NullBooleanField()
    calle = models.CharField(max_lenght=40)
    codigo_postal = models.ForeignKey(Ubicacion, related_name='codigo_postal')

    def _self_(self):
        return self.email

class Evento(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='id')
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    calle = models.CharField(max_lenght=40)
    codigo_postal = models.ForeignKey(Ubicacion, related_name='codigo_postal')
    numero_meseros = models.IntegerField()

#aqui falta un metodo que retorne las horas trabajadas en el evento

class EventoUsuario(models.Model):
    evento = models.ForeignKey(Evento, related_name='id')
    usuario = models.ForeignKey(Usuario, related_name='id')
    aceptado = models.BooleanField()

class Rating(models.Model):
    de_usuario = models.ForeignKey(Usuario, related_name='id')
    hacia_usuario = models.ForeignKey(Usuario, related_name='id')
    rating = models.IntegerField()

class Ubicacion(models.Model):
    codigo_postal = models.IntegerField()
    ciudad = models.CharField(max_lenght=40)
    estado = models.CharField(max_lenght=40)
    pais = models.CharField(max_lenght=30)