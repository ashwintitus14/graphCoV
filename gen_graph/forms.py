from django import forms
from .models import Person
from .models import Link

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
    
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'