#program demos and playing around 
#testing the implementation
import graph_theory_implementaion_1.DrawGraph as DG
#import StaticGraphs as SG

g = { "a" : {"d", "f"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c", "f"},
      "e" : {"c"},
      "f" : {"a", "d"}
    }

#graph = DG.Graph(g)
graph = DG.Graph2(g)

#playing around
#shows edges of a vertix
#for vertice in graph:
#    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))



#adding edges
#graph.add_edge({"ab", "fg"})
#graph.add_edge({"xyz", "bla"})

#shows all vertices and edges of a graph
#print("")
#print("Vertices of graph:")
#print(graph.all_vertices())

#print("Edges of graph:")
#print(graph.all_edges())

#add another vertex and edge to the graph

#print("Add vertex:")
#graph.add_vertex("z")

#print("Add an edge:")
#graph.add_edge({"a", "d"})

#print("Vertices of graph:")
#print(graph.all_vertices())

#print("Edges of graph:")
#print(graph.all_edges())

#again
#print('Adding an edge {"x","y"} with new vertices:')
#graph.add_edge({"x","y"})
#print("Vertices of graph:")
#print(graph.all_vertices())
#print("Edges of graph:")
#print(graph.all_edges())

#paths
#print("Vertices of graph:")
#print(graph.all_vertices())
#print("Edges of graph:")
#print(graph.all_edges())

#print('The path from vertex "a" to vertex "b":')
#path = graph.find_path("a", "b")
#print(path)

#print('The path from vertex "a" to vertex "f":')
#path = graph.find_path("a", "f")
#print(path)

#print('The path from vertex "c" to vertex "c":')
#path = graph.find_path("c", "c")
#print(path)
#print('All paths from vertex "a" to vertex "b":')
#path = graph.find_all_paths("a", "b")
#print(path)
#print('All paths from vertex "a" to vertex "f":')
#path = graph.find_all_paths("a", "f")
#print(path)
#print('All paths from vertex "c" to vertex "c":')
#path = graph.find_all_paths("c", "c")
#print(path)

#degree and degree sequences
print(graph.degree_sequence())
