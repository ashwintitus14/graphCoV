from django.db import models
from django.forms import ModelForm

# Create your models here.

class Person(models.Model):

    p_id = models.CharField(max_length=10, help_text='Patient/Contact ID', primary_key=True)
    
    DISTRICT_CHOICES = [
        ('TVM', 'Thiruvananthapuram'),
        ('KLM', 'Kollam'),
        ('PTA', 'Pathanamthitta'),
        ('ALP', 'Alappuzha'),
        ('KTM', 'Kottayam'),
        ('IDK', 'Idukki'),
        ('EKM', 'Ernakulam'),
        ('TSR', 'Thrissur'),
        ('PKD', 'Palakkad'),
        ('MLPM', 'Malappuram'),
        ('KKD', 'Kozhikode'),
        ('WYD', 'Wayanad'),
        ('KNR', 'Kannur'),
        ('KSD', 'Kasaragod'),
        ('Other State', 'Other State'),
    ]
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    
    STATUS_CHOICES = [
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Awaiting result', 'Awaiting result'),
        ('Not tested', 'Not tested'),
        ('Recovered', 'Recovered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not tested')

    def __str__(self):
        return f'{self.p_id}'

class Link(models.Model):

    #cid = models.CharField(max_length=10, help_text='Contact ID of person1 and person2', default='0')
    person1 = models.CharField(max_length=10, help_text='Patient/Contact ID of person 1')
    person2 = models.CharField(max_length=10, help_text='Patient/Contact ID of person 2')

    def __str__(self):
        #return f'{self.cid}, {self.person1}, {self.person2}'
        return f'{self.person1}, {self.person2}'