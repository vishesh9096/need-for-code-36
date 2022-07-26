from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse("this is index page")

def homepage(request):
    return render(request,'homepage.html')

