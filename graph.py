"""
A python implementation of a graph class.
Demonstrates the functionalities of graphs.

Used the example from https://www.python-course.eu/graphs_python.php as a template.
"""

class Graph(object):

	def __init__(self, dict=None):
		"""
		Initializes the graph dictionary with the inputted dictionary.
		If no dictionary is present, then initialize with an empty one.
		"""
		if dict == None:
			__graph_dict = {}
		else:
			self.__graph_dict = dict

	def vertices(self):
		"""
		Returns the vertices of the graph.
		"""
		return list(self.__graph_dict.keys())

	def edges(self):
		"""
		Returns the edges of the graph.
		"""
		return self.__generate_edges()

	def addVertex(self, vertex):
		"""
		If the vertex is not in the dictionary, then add 
		a key "vertex" with an empty list value.
		"""
		if vertex not in self.__graph_dict:
			self.__graph_dict[vertex] = []

	def addEdge(self, edge):
		"""
		If the edge is not in the dictionary, then add it.
		"""
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.__graph_dict:
			self.__graph_dict[vertex1].append(vertex2)
		else:
			self.__graph_dict[vertex1] = [vertex2]

	def __generate_edges(self):
		"""
		Generates the edges of the graph.
		Edges are represented as sets with one (loops back to vertex) or two vertices.
		"""
		edges = []

		for vertex in self.__graph_dict:
			for neighbor in self.__graph_dict[vertex]:
				if {vertex, neighbor} not in edges:
					edges.append({vertex, neighbor})
		return edges

	def __str__(self):
		res = 'Vertices: '
		for k in self.__graph_dict:
			res += k + ' '
		res += '\nEdges: '
		for edge in self.__generate_edges():
			res += edge
		return res


	def find_path(self, start_vertex, end_vertex, path=None):
		"""
		Find a path from start_vertex to end_vertex in a graph.
		"""
		if path == None:
			path = []
		graph = self.__graph_dict
		path += [start_vertex]
		if start_vertex == end_vertex:
			return path
		if start_vertex not in graph:
			return None
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_path = self.find_path(vertex, end_vertex, path)

				if extended_path:
					return extended_path
		return None




if __name__ == "__main__":
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    graph = Graph(g)

    print 'Path from \'a\' to \'b\': '
    print graph.find_path("a", "b")

'''   print("Vertices of graph:")
       print(graph.vertices())
   
       print("Edges of graph:")
       print(graph.edges())
   
       print("Add vertex:")
       graph.addVertex("z")
   
       print("Vertices of graph:")
       print(graph.vertices())
    
       print("Add an edge:")
       graph.addEdge({"a","z"})
       
       print("Vertices of graph:")
       print(graph.vertices())
   
       print("Edges of graph:")
       print(graph.edges())
   
       print('Adding an edge {"x","y"} with new vertices:')
       graph.addEdge({"x","y"})
       print("Vertices of graph:")
       print(graph.vertices())
       print("Edges of graph:")
       print(graph.edges())'''

