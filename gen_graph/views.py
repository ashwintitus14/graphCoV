from django.shortcuts import render
from .models import Person, Link

# Create your views here.
def index(request):
    """View function for homepage"""

    num_persons = Person.objects.all().count()
    num_links = Link.objects.all().count()

    context = {
        'num_persons': num_persons,
        'num_links': num_links,
    }

    return render(request, 'index.html', context=context)