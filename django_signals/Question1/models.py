from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received. Processing...")
    time.sleep(5)  # Simulate a delay to show the synchronous nature
    print("Signal processing completed.")
