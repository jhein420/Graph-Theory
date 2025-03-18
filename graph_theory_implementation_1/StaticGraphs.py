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

#graph for testing paths

gp = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }

gp1 = { "a" : {"d", "f"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c", "f"},
      "e" : {"c"},
      "f" : {"a", "d"}
    }

#degree and degree sequences
gd = { "a" : {"d", "f"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {"d"}
    }

gd1 = { "a" : {"d", "f"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c", "f"},
      "e" : {"c"},
      "f" : {"a", "d"}
    }
