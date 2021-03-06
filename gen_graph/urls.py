from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('graph', views.show_graph, name='show_graph'),
    path('add_person', views.add, name='add_person'),
    path('add_link', views.link, name='add_link'),
    path('interactive', views.interactive, name='interactive'),
    path('contact', views.contact, name='contact'),
    path('instructions', views.instructions, name='instructions')

]