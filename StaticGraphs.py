# file contains a collection of graphs for use my testing ect...
""" Contains static graphs for testing and control"""


# undirected simple graph
g = { "a" : {"d"},
        "b" : {"c"},
        "c" : {"b", "c", "d", "e"},
        "d" : {"a", "c"},
        "e" : {"c"},
        "f" : {}
    }