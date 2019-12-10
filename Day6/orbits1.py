import networkx as nx

TARGET = 'COM'

with open('input.data','r') as f:
    orbitsMap = [line.strip('\n') for line in f.readlines()]

    tree = nx.Graph()
    for orbit in orbitsMap:
        orbits = orbit.split(')')[1]
        orbited = orbit.split(')')[0]
        
        tree.add_edge(orbited,orbits)
    
    numOrbits = 0
    for node in tree.nodes:
        numOrbits += nx.dijkstra_path_length(tree,node,TARGET)

    print('Total number of orbits: {}'.format(numOrbits))