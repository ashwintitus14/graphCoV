from django.contrib import admin

# Register your models here.

from .models import Person, Link

admin.site.register(Person)
admin.site.register(Link)