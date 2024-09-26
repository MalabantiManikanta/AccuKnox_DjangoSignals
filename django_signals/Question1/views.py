from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from django.shortcuts import render
from Question1.models import MyModel

def create_object(request):
    obj = MyModel(name="Test from View")
    obj.save()  # This will trigger the signal
    return HttpResponse("Object is created successfully")
