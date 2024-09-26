from django.urls import path
from . import views

urlpatterns = [
    path('Q1/', views.create_object, name='create-object'),  # URL pattern for /Q1/
]
