from django.contrib import admin

# Register your models here.

from .models import Person, Links

admin.site.register(Person)
admin.site.register(Links)