from collections import deque
def bfs(graph, start, key):
    found=False
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex,end="\t")
            queue.extend(graph[vertex] - visited)
            if key==vertex:
                found=True
                return found
    return found
    

graph = {}

def add_edge(u, v):
    if u not in graph:
        graph[u] = set()
    graph[u].add(v)

def add_vertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = set()
    
vertices=int(input("Enter the no of vertices : "))

for i in range(vertices):
    print()
    u=input(f"Enter the name of vertex :")
    edges=int(input(f"Enter the no of edges for vertex {u} :"))
    if edges==0:
        add_vertex(graph,u)
    for j in range(edges):
        v=input(f"Enter the child vertex no {j+1} for vertex {u} : ")
        add_edge(u,v)

print()
start_vertex =input(f"Enter the name of start vertex :")
key=input("Enter the vertex to search:")  
print("BFS traversal : ",end="")  
found= bfs(graph, start_vertex, key)
print()
if(found==True):
    print(f"Key {key} found")
else:
    print(f"Key {key} not found")
