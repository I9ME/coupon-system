from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from cupom_sys.models import *
from .forms import *

def post_create(request):#C
	form=PostForm()
	context={
	   "form":form,
	}
	return render(request, "post_form.html", context)


def post_index(request): #R
	queryset=Promotion.objects.all()
	context={
	   "object_list": queryset,
	}
	return render(request, "index.html", context)

def post_detail(request,t_id):
	instance= get_object_or_404(Promotion, id=t_id)
	context={
	   "item": instance,
	}
	return render(request, "details.html", context)