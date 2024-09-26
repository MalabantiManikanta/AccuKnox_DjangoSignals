from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from django.shortcuts import render
from Question2.models import MyModel

def my_signal_handler(request):
    print(f"Saving object in thread:")
    obj = MyModel(name="Test from View")
    obj.save()  # This will trigger the signal
    return HttpResponse("Object is created successfully...")
