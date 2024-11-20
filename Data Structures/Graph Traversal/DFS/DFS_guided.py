from collections import defaultdict
from typing import List, Set


class Graph:
    def __init__(self):
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
    Perform DFS traversal recursively starting from start_vertex.
    :param start_vertex: -> int
    :return list of vertices in DFS order: -> List[int]
    """
    def dfs_recursive(self, start_vertex: int) -> List[int]:
        # Keep track of visited vertices
        visited = set()

        # Result list to store DFS traversal order
        result = []
        
        # Helper method in scope to store values over steps
        def dfs_helper(vertex: int) -> None:
            # Mark current vertex as visited and add to result
            
            # Recur for all adjacent vertices
            pass
        
        dfs_helper(start_vertex)

        # Return result
        pass
    

    """
    Perform DFS traversal iteratively using a stack.
    :param start_vertex: -> int
    :return list of vertices in DFS order: -> List[int]
    """
    def dfs_iterative(self, start_vertex: int) -> List[int]:
        # Keep track of visited vertices

        # Push starting vertex to populate stack

        # Result list to store vertices in DFS order
        
        # While stack is populated

        # Pop the next vertex from stack
        
        # Mark current vertex as visited and add to result
        
            
        # Add neighbors to stack in reverse order
        # (to match recursive DFS order)
            
        # Return result
        pass


# Example usage:
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    
    # Add edges (creating this graph structure):
    #     0 -----> 1
    #     |        |
    #     v        v
    #     2 -----> 3
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    
    # Test recursive DFS
    print("DFS recursive starting from vertex 0:")
    dfs_recursive_result = g.dfs_recursive(0)
    print(dfs_recursive_result)  # Output: [0, 1, 3, 2]
    
    # Test iterative DFS
    print("\nDFS iterative starting from vertex 0:")
    dfs_iterative_result = g.dfs_iterative(0)
    print(dfs_iterative_result)  # Output: [0, 1, 3, 2]
    
    # Example with a more complex graph
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)
    g2.add_edge(2, 3)
    g2.add_edge(3, 3)
    
    print("\nComplex graph DFS recursive starting from vertex 2:")
    print(g2.dfs_recursive(2))  # Output: [2, 0, 1, 3]
