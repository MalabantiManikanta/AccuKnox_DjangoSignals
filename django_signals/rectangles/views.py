from django.shortcuts import render

# Create your views here.
# rectangles/views.py
from django.http import JsonResponse
from rectangles.models import Rectangle  # Import the Rectangle class

def rectangle_view(request):
    # Example values for length and width
    length = 5
    width = 10
    
    # Create an instance of Rectangle
    rect = Rectangle(length, width)
    
    # Collect the rectangle dimensions in a list
    dimensions = list(rect)  # Convert iterator to a list
    
    return JsonResponse(dimensions, safe=False)  # Return dimensions as JSON
