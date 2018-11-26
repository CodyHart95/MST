'''
Cody Hart
Tom Manser
Drew Waszak
'''

import sys
def minKey(G,mstSet):
     min_value = sys.maxsize
     min_key = -1
     for i in mstSet:
         for v in G[i]:       
            if v[1] < min_value and v[0] not in mstSet:
                min_value = v[1]
                min_key = v[0]
             
     return min_key,min_value

def prims(G,vertex):     
    mstSet = []
    mstSet.append(vertex)
    edge_lengths = 0
    i = 0
    while len(mstSet) < len(G):
        min_key,min_value = minKey(G,mstSet)
        mstSet.append(min_key)
        edge_lengths += min_value

    return edge_lengths

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
