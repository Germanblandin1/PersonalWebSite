from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.shortcuts import render
from django.template import loader
# Create your views here.
app_name="blogs"

def index(request):
	return render(request,app_name+'/index.html')