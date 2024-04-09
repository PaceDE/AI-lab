def dfs(graph, vertex, visited,key):
    visited.add(vertex)
    print(vertex,end="\t")
    if (key==vertex):
        return True
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, visited,key):
                return True
                    
    return False

graph = {}

def add_edge(u, v):
    if u not in graph:
        graph[u] = set()
    graph[u].add(v)

def add_vertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = set()

vertices = int(input("Enter the number of vertices:"))

for i in range(vertices):
    print()
    u=input(f"Enter the name of vertex :")
    edges = int(input(f"Enter the number of edges for vertex {u}: "))
    if edges == 0:
        add_vertex(graph, u)
    for j in range(edges):
        v=input(f"Enter the child vertex no {j+1} for vertex {u} : ")
        add_edge(u,v)

print()
start_vertex = input("Enter the starting vertex: ")
key=input("Enter the vertex to search:") 
print()
print("DFS traversal : ",end="")
visited = set()
found=dfs(graph, start_vertex, visited,key)
print()
if found:
        print(f"Key {key} found")
else:
        print(f"Key {key} not found")