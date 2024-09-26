from django.db import models
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal running within the transaction.")
    else:
        print("Signal running outside of the transaction.")
# Create your models here.
