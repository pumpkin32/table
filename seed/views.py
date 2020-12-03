from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import db

def index(request):
	press = db.objects.all()
	return render(request, 'index.html', {"press":press})

def ADD(request):
	if request.method == "POST":
		press = db()
		press.content = None
		press.save()
		return HttpResponseRedirect("/")
	
def DEL(request):
	if request.method == "POST":
		press = db.objects.last()
		press.delete()
		return HttpResponseRedirect("/")