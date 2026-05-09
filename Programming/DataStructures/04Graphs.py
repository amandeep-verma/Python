"""
Graph — a set of vertices (nodes) connected by edges.

Terminology:
  Vertex (Node) : an entity or point in the graph
  Edge          : a connection between two vertices

Types:
  Directed   : edges have direction (A → B does not imply B → A)
  Undirected : edges are mutual (A — B implies B — A)
  Weighted   : edges carry a cost/distance value
  Sparse     : few edges relative to vertices → use Adjacency List
  Dense      : many edges relative to vertices → use Adjacency Matrix

Representations:
  Edge List       : [(u,v), ...] — simple but slow lookups O(E)
  Adjacency Matrix: 2D array M[u][v] = 1 if edge exists — O(1) lookup, O(V²) space
  Adjacency List  : {v: [neighbours]} — O(V+E) space, efficient for sparse graphs ✓

This implementation uses an Adjacency List via Node.neighbors.
Edges are directed by default — uncomment node2.neighbors.append(node1) for undirected.

DFS — Depth First Search: explores as deep as possible before backtracking.
      Uses a stack (iterative) or call stack (recursive).
      Good for: cycle detection, topological sort, connected components.
      Time: O(V+E) | Space: O(V) for visited set + stack

BFS — Breadth First Search: explores all neighbours at current depth before going deeper.
      Uses a queue.
      Good for: shortest path (unweighted), level-order traversal.
      Time: O(V+E) | Space: O(V) for visited set + queue

For adjacency list, V = number of vertices, E = number of edges.
| Operation    | Time   | Space |
|--------------|--------|-------|
| addNode      | O(1)   | O(1)  |
| addEdge      | O(1)   | O(1)  |
| dfsRecursive | O(V+E) | O(V)  |
| dfsIterative | O(V+E) | O(V)  |
| bfsIterative | O(V+E) | O(V)  |

Tree is a graph with below properties:
1. It is a connected graph (You can reach any vertex from any other vertex).
2. It has no cycles.
3. It has n-1 edges where n is the number of vertices.
"""

from collections import deque

class Graph:

    class Node:
        def __init__(self, data=None):
            self.data = data
            self.neighbors = []

    def __init__(self):
        self.nodes = []

    def addNode(self, data):
        newNode = self.Node(data)
        self.nodes.append(newNode)
        return newNode

    def addEdge(self, node1, node2):
        node1.neighbors.append(node2)   # directed: node1 → node2
        # node2.neighbors.append(node1) # uncomment for undirected

    # Time: O(V+E) | Space: O(V) — call stack depth up to V in worst case
    def dfsRecursiveHelper(self, node, visited, result):
        visited.add(node)
        result.append(node.data)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                self.dfsRecursiveHelper(neighbor, visited, result)

    def dfsRecursive(self, start):
        """Explore deep via call stack; risk of stack overflow on very large graphs."""
        visited = set()
        result = []
        self.dfsRecursiveHelper(start, visited, result)
        return result

    # Time: O(V+E) | Space: O(V) — explicit stack on heap, safer than recursion
    def dfsIterative(self, start):
        """Push neighbours onto stack; pop and visit — right neighbour pushed first
        so left is processed first (mirrors recursive order)."""
        visited = set()
        result = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node.data)
                for neighbor in reversed(node.neighbors):  # reverse to preserve order
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    # Time: O(V+E) | Space: O(V) — queue holds all nodes at current frontier
    def bfsIterative(self, start):
        """Explore level by level via queue; guarantees shortest path in unweighted graphs."""
        visited = set()
        result = []
        queue = deque()
        queue.append(start)
        visited.add(start)
        while queue:
            node = queue.popleft()
            result.append(node.data)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)   # mark on enqueue, not on visit
                    queue.append(neighbor)  # prevents duplicate entries in queue
        return result


# Build graph:  0 → 1 → 3
#               ↓       ↑
#               2 ──────┘
myGraph = Graph()
n0 = myGraph.addNode(0)
n1 = myGraph.addNode(1)
n2 = myGraph.addNode(2)
n3 = myGraph.addNode(3)

print("Adding edge 0 → 1:", myGraph.addEdge(n0, n1))
print("Adding edge 0 → 2:", myGraph.addEdge(n0, n2))
print("Adding edge 1 → 3:", myGraph.addEdge(n1, n3))
print("Adding edge 2 → 3:", myGraph.addEdge(n2, n3))

print("DFS Recursive from 0:", myGraph.dfsRecursive(n0))
print("DFS Iterative from 0:", myGraph.dfsIterative(n0))
print("BFS Iterative from 0:", myGraph.bfsIterative(n0))