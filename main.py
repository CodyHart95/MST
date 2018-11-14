'''
Cody Hart
Tom Manser
Drew Waszak
'''

import sys
def minKey(G,key,mstSet):
     min_value = sys.maxsize
     min_key = -1
     for v in range(len(G[key])):
         if G[key][v][1] < min_value and G[key][v][0] not in mstSet:
             min_value = G[key][v][1]
             min_key = v
             
     return min_key

#To make this work for the rest of the inputs remove inner for loop.
def prims(G,vertex):
    print(G)
    mstSet = []
    mstSet.append(vertex)
    edge_lengths = [0 for i in range(0,len(G)+1)]

    for v in mstSet:
        for edge in G[v]:
            min_key = minKey(G,v,mstSet)
            if min_key > -1:
                mstSet.append(G[v][min_key][0])
                edge_lengths[G[v][min_key][0]] = (G[v][min_key])
        print(mstSet)
    mst_length = 0
    
    '''
    for i in edge_lengths:
        mst_length += i 
    return mst_length
    '''

def add_edge(G, v1, v2, ce):
    if v1 in G:
        G[v1].append((v2, ce))
    else:
        G[v1] = [(v2, ce)]
    if v2 in G:
        G[v2].append((v1, ce))
    else:
        G[v2] = [(v1, ce)]


if __name__ == '__main__':

    input_filename = input('Please provide an input filename:\n')
    input_vertex = int(input('Please provide a start vertex label (1..n):\n'))

    G = {}
    with open(input_filename, 'r') as input_graph_file:
        n, m = tuple(int(x) for x in input_graph_file.readline().split())
        G = {}
        for line in input_graph_file:
            v1, v2, ce = tuple(int(v) for v in line.split())
            add_edge(G, v1, v2, ce)

    print(prims(G, input_vertex))