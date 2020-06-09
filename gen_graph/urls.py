from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graph', views.show_graph, name='show_graph')
]