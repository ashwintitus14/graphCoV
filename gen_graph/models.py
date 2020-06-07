from django.db import models

# Create your models here.

class Person(models.Model):

    p_id = models.CharField(max_length=10, help_text='Patient/Contact ID', primary_key=True)
    tested_positive = models.BooleanField(default=False, help_text='True if person is COVID 19 positive')

    def __str__(self):
        return f'{self.p_id}'

class Link(models.Model):

    person1 = models.CharField(max_length=10, help_text='Patient/Contact ID of person 1')
    person2 = models.CharField(max_length=10, help_text='Patient/Contact ID of person 2')

    def __str__(self):
        return f'{self.person1}, {self.person2}'
