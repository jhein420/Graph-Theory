#for testing and checking with hardcoded data
#basic graph using dictionaries

graph = { "a" : {"c"},
          "b" : {"c", "e"},
          "c" : {"a", "b", "d", "e"},
          "d" : {"c"},
          "e" : {"c", "b"},
          "f" : {}
        }



#fucntions for display and checking
#Function to generate the list of all edges 
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append({node, neighbour})

    return edges

  # returns a set of isolated nodes. 
def find_isolated_nodes(graph):
 
    isolated = set()
    for node in graph:
        if not graph[node]:
            isolated.add(node)
    return isolated

#log graph dict
def ShowGraph(a):
    print(a)


#display to console or GUI

ShowGraph(graph)
print('Isolated Nodes', find_isolated_nodes(graph))
print('Edges', generate_edges(graph))