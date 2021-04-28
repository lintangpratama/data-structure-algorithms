# Graph
# Adjacency List

class Graph:
  def __init__(self):
    self.graph = {}
    
  # make the add_vertex method  
  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = []
    else: 
      print(f"Vertex {vertex} is already exist.")
  
  # make the add_edge method
  def add_edge(self, vertex1, vertex2, edge):
    if vertex1 not in self.graph:
      print(f"Vertex {vertex1} doesn't exist.")
    elif vertex2 not in self.graph:
      print(f"Vertex {vertex2} doesn't exist.")
    else:
      temp = [vertex2, edge]
      self.graph[vertex1].append(temp)

  # make the display method to print the whole graph
  def display(self):
    for vertex in self.graph:
      for edge in self.graph[vertex]:
        print(f"{vertex} -> {edge[0]} edge weight: {edge[1]}")
    print(f"Internal representation: {self.graph}")

def main()
  # init the graph and vertex
  graph_list = Graph()
  graph_list.add_vertex(1)
  graph_list.add_vertex(2)
  graph_list.add_vertex(3)
  graph_list.add_vertex(4)

  # edge initialization
  graph_list.add_edge(1, 2, 2)
  graph_list.add_edge(1, 3, 2)
  graph_list.add_edge(2, 3, 4)
  graph_list.add_edge(3, 4, 5)
  graph_list.add_edge(4, 1, 6)

  # Print the whole graph_list
  graph_list.display()

if __name__ = '__main__':
  main()