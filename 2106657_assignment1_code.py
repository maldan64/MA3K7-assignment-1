### IMPORTANT PLEASE READ FIRST ###
### NETWORKX VERSION MUST BE 3.0.0 OR HIGHER TO RUN THE CODE!!!!


# necessary libraries 
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Ddefining function which will output bracelet array
def  make_bracelet(a,b):
    
# converting input to correct form (modulo 10)
    a = a % 10
    b = b % 10
    
# preliminary bracelet array
    brac = [a,b]
    
# variables to control how the loop checks presence of double pair
    index = 1
    same_pair = 0
    
    while same_pair != 1:

# the next entry in the bracelet being generated (addition modulo 10)
        c = (brac[index -1] + brac[index]) % 10

# checking this doesn't cause a double pair
        if str(brac[index])+ str(c) == str(a) + str(b):
            same_pair = 1
            
# adding it to the list if it doesn't cause a double pair
        else:
            brac.append(c)
            index = index + 1
    return brac

# taking the initial integers as input
a = int(input("Please input the first integer of the bracelet"))
b = int(input("Please input the second integer of the bracelet"))

# extracting array from function
brac  = make_bracelet(a,b)
print("Your bracelet is",brac)

# a dictionary for use in labelling vertices of bracelet
my_dict = {}
for index, element in enumerate(brac):
    my_dict[index] = str(element)
    
# removing the last item so the bracelet can loop correctly
my_dict.popitem()

# generating visual bracelet
G = nx.Graph()

# a simple array so the correct amount of vertices and edge are added
labels = np.arange(0,len(brac),1)

# adding all the vertices and edges to the graph
for i in range(0,len(brac)-1):
    G.add_node(labels[i])
    if i > 0:
        G.add_edge(labels[i],labels[i-1])

G.add_edge(labels[0],labels[len(labels)-2])

# plotting a circular graph with the correct labels and # of vertices
nx.draw_circular(G, labels = my_dict, node_color = '#eb5ec5')
plt.show()
