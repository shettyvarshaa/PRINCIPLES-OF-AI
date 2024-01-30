graph = {
    '1' : ['2','3'],
    '2' : ['4', '5'],
    '3' : ['6','7'],
    '4' : [],
    '5' : [],
    '6' : [],
    '7' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("here is the code for breadth first search")
bfs(visited,graph,'1')  # call function with starting node as '1
print()

graph2 = {
    '1' : ['2','3'],
    '2' : ['4', '5'],
    '3' : ['6','7'],
    '4' : [],
    '5' : [],
    '6' : [],
    '7' : []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph2[node]:
            dfs(visited,graph,neighbour)

print("here is the code for depth first search")
dfs(visited,graph2,'1')   # call function with starting node as '1