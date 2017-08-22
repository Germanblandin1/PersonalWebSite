from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Blog
from .forms import BlogForm
# Create your views here.
app_name="blogs/"

def index(request):
	return render(request,app_name+'index.html')


def manage_views(request):
	str_aux=request.path[1:request.path.__len__()]
	print(str_aux)
	template=loader.get_template(str_aux)
	seccion="Othessr"
	subseccion="Pitem"
	titulo="Blogs"
	context={
		'seccion': seccion,
		'titulo': titulo,
		'subseccion': subseccion
	}
	return HttpResponse(template.render(context,request))
	#return render(request, str_aux,context)
	
def blogs_view(request):
	list_blog=Blog.objects.all()
	context={
		'titulo': "Blogs",
		'blogs': list_blog
	}
	return render(request, app_name+'/blog-home-1.html',context)

def blog_detail_view(request, pk):
	blog= get_object_or_404(Blog, pk=pk)
	titulo="Blogs"
	context={
		'titulo': titulo,
		'blog': blog
	}
	return render(request, app_name+'/blog-post.html',context)
	
def new_blog_view(request):
	if request.method=="POST":
		form= BlogForm(request.POST,request.FILES)
		if form.is_valid():
			blog=form.save()
			blog.save()
			return HttpResponseRedirect("index.html")
		else:
			return HttpResponse("no es valido")
	else:
		form=BlogForm()
	template=app_name+'/new_blog.html'
	context={
		'titulo': 'Agrega un nuevo blog',
		'form': form
	}
	return render(request, template,context)