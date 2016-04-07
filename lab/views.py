from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, 'lab/base.html')

def aboutus(request):
	return render(request, 'lab/aboutus.html')

def contactus(request):
	return render(request, 'lab/contactus.html')

def learn(request):
	return render(request, 'lab/learn.html')

def live(request):
	return render(request, 'lab/live.html')

def play(request):
	return render(request, 'lab/play.html')

def reduce(request):
	return render(request, 'lab/reduce.html')

def makeit(request):
	return render(request, 'lab/makeit.html')

def yorkland(request):
	return render(request, 'lab/yorkland.html')


