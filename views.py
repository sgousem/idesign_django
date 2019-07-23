from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def idesign(request):
    flist = Feature.objects.all()
    return render(request,'index1.html',{'flist':flist})