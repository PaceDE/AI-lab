from queue import PriorityQueue

def astar(graph, start, target):
    visited = set()
    queue = PriorityQueue()
    queue.put((0 + graph[start]['heuristic'], 0, start))  # (f, g, node)
    while not queue.empty():
        _, cost, current = queue.get()
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
                g = cost + neighbors[neighbor]  # Actual cost from start to neighbor
                queue.put((g + graph[neighbor]['heuristic'], g, neighbor))  # Add neighbor to the priority queue
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
print("Enter edges (format: source_vertex target_vertex cost): ")
for _ in range(edges):
    source, target, cost = input().split()
    cost = int(cost)
    if source not in graph:
        print(f"Vertex {source} not found in the graph. Skipping edge input.")
        continue
    if target not in graph:
        print(f"Vertex {target} not found in the graph. Skipping edge input.")
        continue
    graph[source].setdefault('neighbors', {}).update({target: cost})

start_node = input("Enter the start node: ")
target_node = input("Enter the target node: ")

print("A* traversal:", end=" ")
if astar(graph, start_node, target_node):
    print("\nTarget node found")
else:
    print("\nTarget node not found")
