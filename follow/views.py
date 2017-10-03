from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'follow/index.html')

def acces(request):
	return render(request, 'follow/acces.html')