from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Person, Link
from django.urls import reverse

import networkx as nx
import matplotlib.pyplot as plt

from networkx.readwrite import json_graph # To convert graph to JSON and vice versa
import json
import os.path

G = nx.Graph()

# Create your views here.
def index(request):
    if os.path.exists('gen_graph/data/graph.json') == False:
        print("File does not exists/Graph not yet generated") # Redirect to page with message, "Graph is empty"
        return render(request,'not_generated.html')
    else:
        H = nx.Graph()
        plt.clf()
        with open('gen_graph/data/graph.json') as json_file:
            data = json.load(json_file)
        json_file.close()
        H = json_graph.node_link_graph(data)
        nx.draw(H, with_labels=True, font_color='white')
        plt.savefig('gen_graph/static/path.png')
    
    return render(request,'index.html')

from .forms import PersonForm        

def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'add.html', {'form': form})
    else:
        form = PersonForm()
        return render(request,'add.html', {'form': form})

from .forms import LinkForm

def link(request):
    if request.method == "POST":
        forml = LinkForm(request.POST)
        if forml.is_valid():
            forml.save()
            return render(request, 'graph.html')
    else:
        return render(request,'CoVform3.html')

def contact(request):
    return render(request,'CoVcontact.html')

def instruction(request):
    return render(request,'CoVinstruction.html')

def index1(request):
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


    # To convert to JSON
    from networkx.readwrite import json_graph
    data1 = json_graph.node_link_data(G)
    import json
    s1 = json.dumps(data1)
    print(s1)
    # To save JSON data to a file
    with open('gen_graph/data/graph.json', 'w') as outfile:
        json.dump(data1, outfile)
    # To read from JSON file to graph object
    from networkx.readwrite import json_graph
    import json
    with open('gen_graph/data/graph.json') as json_file:
        data = json.load(json_file)
    H = json_graph.node_link_graph(data)
    print(H.nodes)
    print(H.edges)



    #print(G.nodes)
    #print(G.edges)

    #rint(links, persons)

    nx.draw(G, with_labels=True, font_color='white')
    plt.savefig('gen_graph/static/path.png')

    return render(request, 'index.html', context=context)

def show_graph(request):
    """View function for graph display page"""

    return render(request, 'graph.html')