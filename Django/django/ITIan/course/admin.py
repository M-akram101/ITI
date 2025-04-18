from django.contrib import admin


# Register your models here.
from .models import Course  # Import your model

admin.site.register(Course)  # Register the model
