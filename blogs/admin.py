from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Usuario)
class AdminUser(admin.ModelAdmin):
	list_display=('id','nombre')
	
@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
	list_display=('id','titulo',)
	list_filter=('categorias',)
	
@admin.register(Pais)
class AdminPais(admin.ModelAdmin):
	list_display=('id','nombre')

@admin.register(Habilidad)
class AdminHabilidad(admin.ModelAdmin):
	list_display=('id','nombre',)

@admin.register(Posee)
class AdminPosee(admin.ModelAdmin):
	list_display=('id','usuario_id','habilidad_id','nivel',)
	list_filter=('habilidad_id','usuario_id',)

@admin.register(Categoria)
class AdminPosee(admin.ModelAdmin):
	list_display=('id','nombre',)

@admin.register(Pertenece)
class AdminPosee(admin.ModelAdmin):
	list_display=('id','categoria_id','blog_id',)
	list_filter=('categoria_id','blog_id',)
