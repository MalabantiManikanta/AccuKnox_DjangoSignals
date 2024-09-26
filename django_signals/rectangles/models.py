from django.db import models

# Create your models here.
# rectangles/rectangle.py

class Rectangle:
    def __init__(self, length: int, width: int):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive integers.")
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
