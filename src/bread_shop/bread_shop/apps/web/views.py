from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
	context = {}
	context['name'] = 'Hello World!'
	return render(request,"hello.html",context)


