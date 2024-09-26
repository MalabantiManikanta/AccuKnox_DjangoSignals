from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")