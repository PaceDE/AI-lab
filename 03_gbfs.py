from collections import deque

def gbfs(graph, start, target):
    visited = set()
    queue = deque([(0, start)])  # Priority queue with priority as heuristic value
    while queue:
        _, current = queue.popleft()  # Pop the node with the lowest heuristic value
        visited.add(current)
        print(current, end=" ")  # Print the current node
        if current == target:
            return True
        print(" -> ",end="")
        neighbors = graph.get(current, {}).get('neighbors', {})
        for neighbor, heuristic_value in neighbors.items():
            if neighbor not in visited:
                if 'heuristic' not in graph.get(neighbor, {}):
                    print(f"Heuristic value not provided for vertex {neighbor}. Skipping.")
                    continue
                queue.append((graph[neighbor]['heuristic'], neighbor))  # Add neighbors to the priority queue
                queue = deque(sorted(queue, key=lambda x: x[0]))  # Sort the queue based on heuristic value
    return False

# Take input for the graph
graph = {}
vertices = int(input("Enter the number of vertices: "))

# Input heuristic values for each vertex
print("Enter heuristic value for each vertex:")
for _ in range(vertices):
    vertex, heuristic_value = input("Enter vertex and its heuristic value (format: vertex heuristic_value): ").split()
    graph[vertex] = {'heuristic': int(heuristic_value)}

# Input edges
edges = int(input("Enter the number of edges: "))
print("Enter edges (format: source_vertex target_vertex): ")
for _ in range(edges):
    source, target = input().split()
    if source not in graph:
        print(f"Vertex {source} not found in the graph. Skipping edge input.")
        continue
    if target not in graph:
        print(f"Vertex {target} not found in the graph. Skipping edge input.")
        continue
    graph[source].setdefault('neighbors', {}).update({target: graph[target]['heuristic']})

start_node = input("Enter the start node: ")
target_node = input("Enter the target node: ")

print("GBFS traversal:", end=" ")
if gbfs(graph, start_node, target_node):
    print("\nTarget node found")
else:
    print("\nTarget node not found")
