from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import  content, rubric

def index(request):
	db = rubric.objects.all()
	return render(request, 'index.html', {'db':db})

def about(request, Title):
	db = rubric.objects.get(title = '{0}'.format(Title))
	DB = db.content_set.all()
	return render(request, 'about.html', {'db':db, 'DB':DB})