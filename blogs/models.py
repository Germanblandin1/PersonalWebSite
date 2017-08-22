from django.db import models

# Create your models here.
class Pais(models.Model):
	nombre=models.CharField(max_length=255)
	def __str__(self):
		return self.nombre

class Habilidad(models.Model):
	nombre=models.CharField(max_length=255)
	descripcion=models.CharField(max_length=500)
	def __str__(self):
		return self.nombre

	
class Usuario(models.Model):
	nombre=models.CharField(max_length=255)
	apellido=models.CharField(max_length=255)
	direccion=models.CharField(max_length=500)
	correo=models.EmailField(unique=True)
	descripcion=models.CharField(max_length=500)
	profesion=models.CharField(max_length=255)
	imagen=models.ImageField(blank=True)
	telefono=models.IntegerField(default=0)
	
	#relaciones
	pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
	habilidades = models.ManyToManyField(Habilidad, through='Posee')
	def __str__(self):
		return self.nombre+self.apellido


class Posee(models.Model):
	usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	habilidad_id = models.ForeignKey(Habilidad, on_delete=models.CASCADE)
	nivel=models.CharField(max_length=50)
	
	def __str__(self):
		return str(self.usuario_id)+"-"+str(self.habilidad_id)
		
class Categoria(models.Model):
	nombre=models.CharField(max_length=255)
	def __str__(self):
		return self.nombre

class Blog(models.Model):
	titulo=models.CharField(max_length=255)
	contenido=models.TextField()
	imagen=models.ImageField(blank=True)
	fecha=models.DateTimeField(auto_now=True)
	
	#relaciones
	categorias = models.ManyToManyField(Categoria, through='Pertenece')
	
	def __str__(self):
		return self.titulo
	class Meta:
		ordering=('id',)

	

	
class Pertenece(models.Model):
	categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.blog_id)+"-"+str(self.categoria_id)
	

	


