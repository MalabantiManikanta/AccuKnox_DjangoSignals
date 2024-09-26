from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from django.shortcuts import render
from Question1.models import MyModel

#from django.http import HttpResponse
#from django.shortcuts import render
#from .models import MyModel
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

def create_object1(request):
    with transaction.atomic():  # Start a transaction block
        obj = MyModel(name="Test from Q1 URL")
        obj.save()  # This will trigger the signal

    return HttpResponse("Trasaction completed..")