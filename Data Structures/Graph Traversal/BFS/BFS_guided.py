from collections import defaultdict, deque
from typing import List, Set

class Graph:
    def __init__(self):
        # Using defaultdict to automatically initialize empty lists for new vertices
        self.graph = defaultdict(list)


    """
    Create a graph of nodes and edges.
    :param vertex: -> int
    :param neighbor: -> int
    :return:
    """
    def add_edge(self, vertex: int, neighbor: int) -> None:
        """Add an edge between vertex and neighbor"""
        self.graph[vertex].append(neighbor)
    

    """
    BFS from start_vertex.
    :param start_vertex: -> int
    :return: list of vertices in BFS order
    """
    def bfs(self, start_vertex: int) -> List[int]:
        # Keep track of visited vertices
        
        # Queue for BFS

        # Result list to store BFS traversal order
        
        # Start with the initial vertex

        # While queue is populated

            # Get the next vertex from queue
            
            
            # Explore neighbors of current vertex
            
        
        # return result
        pass


# Example usage:
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    # Perform BFS starting from vertex 2
    print("BFS starting from vertex 2:")
    bfs_traversal = g.bfs(2)
    print(bfs_traversal)  # Output: [2, 0, 3, 1]
