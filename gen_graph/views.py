import json
import os.path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from networkx.readwrite import json_graph  # To convert graph to JSON and vice versa

from .forms import LinkForm, PersonForm
from .models import Link, Person

G = nx.Graph()

# Create your views here.
def index(request):
    """Reads data from graph.json, renders image of the graph and displays it in the homepage."""
    if os.path.exists('gen_graph/data/graph.json') == False:
        #print("File does not exists/Graph not yet generated")
        return render(request,'not_generated.html')
    else:
        """
        H = nx.Graph()
        plt.clf()
        with open('gen_graph/data/graph.json') as json_file:
            data = json.load(json_file)
        json_file.close()
        H = json_graph.node_link_graph(data)
        print(H)
        """
        H = nx.Graph()
        links = Link.objects.all()
        persons = Person.objects.all()
        
        plt.clf() # Clears the plot
        for person in persons:
            H.add_node(person.p_id, status=person.status)
        
        for link in links:
            H.add_edge(link.person1, link.person2)
        
        color_map = []
        for node in H:
            if H.nodes[node]['status'] == 'Positive':
                color_map.append('red')
            elif H.nodes[node]['status'] == 'Negative':
                color_map.append('green')
            elif H.nodes[node]['status'] == 'Awaiting result':
                color_map.append('blue')
            elif H.nodes[node]['status'] == 'Not tested':
                color_map.append('grey')
            elif H.nodes[node]['status'] == 'Recovered':
                color_map.append('purple')
        num_disconnected_subgraphs = 0 # Number of disconnected subgraphs in the graph
        for c in nx.connected_components(H):
            num_disconnected_subgraphs+=1
        
        #To draw a legend for the graph
        """
        p1 = mpatches.Patch(color='red', label='Positive')
        p2 = mpatches.Patch(color='green', label='Negative')
        p3 = mpatches.Patch(color='blue', label='Awaiting result')
        p4 = mpatches.Patch(color='grey', label='Not tested')
        p5 = mpatches.Patch(color='purple', label='Recovered')
        plt.legend(handles=[p1,p2,p3,p4,p5], loc=(0.80,0.80))
        """
        nx.draw(H, with_labels=True, font_color='white', font_size=7, node_size=350, node_color=color_map)
        plt.savefig('gen_graph/static/path.png', dpi=150)

        context = {
            'num_disconnected_subgraphs' : num_disconnected_subgraphs
        }
    
    return render(request,'index.html', context=context)


def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

            G = nx.Graph()
            links = Link.objects.all()
            persons = Person.objects.all()
            
            plt.clf() # Clears the plot
            for person in persons:
                G.add_node(person.p_id, status=person.status)
            
            for link in links:
                G.add_edge(link.person1, link.person2)


            # To convert to JSON
            #from networkx.readwrite import json_graph
            data1 = json_graph.node_link_data(G)
            #import json
            s1 = json.dumps(data1)
            # To save JSON data to a file
            with open('gen_graph/data/graph.json', 'w') as outfile:
                json.dump(data1, outfile)
            with open('gen_graph/static/graph.json', 'w') as outfile: #For interactive graph page
                json.dump(data1, outfile)



            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'add_person.html', {'form': form})
    else:
        form = PersonForm()
        return render(request, 'add_person.html', {'form': form})


def link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            G = nx.Graph()
            links = Link.objects.all()
            persons = Person.objects.all()
            
            plt.clf() # Clears the plot
            for person in persons:
                G.add_node(person.p_id, status=person.status)
            
            for link in links:
                G.add_edge(link.person1, link.person2)


            # To convert to JSON
            #from networkx.readwrite import json_graph
            data1 = json_graph.node_link_data(G)
            #import json
            s1 = json.dumps(data1)
            # To save JSON data to a file
            with open('gen_graph/data/graph.json', 'w') as outfile:
                json.dump(data1, outfile)
            with open('gen_graph/static/graph.json', 'w') as outfile: # For interactive graph page
                json.dump(data1, outfile)

            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'add_link.html', {'form': form})
    else:
        form = LinkForm()
        return render(request, 'add_link.html', {'form': form} )

def interactive(request):
    return render(request, 'interactive_graph.html')

def contact(request):
    return render(request,'contact.html')

def instructions(request):
    return render(request,'instructions.html')
"""
def index1(request):
    #View function for homepage

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
    #View function for graph display page

    return render(request, 'graph.html')
"""