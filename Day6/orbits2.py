import networkx as nx

YOU = 'YOU'
SANTA = 'SAN'

with open('input.data','r') as f:
    orbitsMap = [line.strip('\n') for line in f.readlines()]

    tree = nx.Graph()
    for orbit in orbitsMap:
        orbits = orbit.split(')')[1]
        orbited = orbit.split(')')[0]
        
        tree.add_edge(orbited,orbits)
    
    print('Minimum number of orbital transfers required: {}'.format(len(nx.dijkstra_path(tree,YOU,SANTA)) - 3))