#program demos and playing around
import DrawGraph as DG
import StaticGraphs as SG

gr = SG.g

graph = DG.Graph(gr)

#playing around
#shows edges of a vertix
for vertice in graph:
    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))



#adding edges
graph.add_edge({"ab", "fg"})
graph.add_edge({"xyz", "bla"})

#shows all vertices and edges of a graph
print("")
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

#add another vertex and edge to the graph

print("Add vertex:")
graph.add_vertex("z")

print("Add an edge:")
graph.add_edge({"a", "d"})

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

#again
print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())

