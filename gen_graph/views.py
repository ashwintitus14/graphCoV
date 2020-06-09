from django.shortcuts import render
from .models import Person, Link

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Create your views here.
def index(request):
    """View function for homepage"""

    num_persons = Person.objects.all().count()
    num_links = Link.objects.all().count()

    context = {
        'num_persons': num_persons,
        'num_links': num_links,
    }

    links = Link.objects.all()
    persons = Person.objects.all()
    
    plt.clf() # Clears the plot
    for person in persons:
        G.add_node(person.p_id)
    
    for link in links:
        G.add_edge(link.person1, link.person2)

    print(G.nodes)
    print(G.edges)

    print(links, persons)

    nx.draw(G, with_labels=True, font_color='white')
    plt.savefig('gen_graph/static/path.png')

    return render(request, 'index.html', context=context)

def show_graph(request):
    """View function for graph display page"""

    return render(request, 'graph.html')