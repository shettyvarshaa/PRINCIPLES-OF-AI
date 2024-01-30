# Define the graph as an adjacency list
graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

# Initialize lists to track visited nodes and the queue for BFS
visited_bfs = []
queue_bfs = []

def bfs(visited, graph, start_node):
    visited.append(start_node)
    queue_bfs.append(start_node)

    while queue_bfs:
        current_node = queue_bfs.pop(0)
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue_bfs.append(neighbour)

print("Breadth First Search:")
bfs(visited_bfs, graph, '1')  # Call function with starting node as '1'
print()

# Define another graph as an adjacency list
graph_dfs = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

# Initialize a set to track visited nodes for DFS
visited_dfs = set()

def dfs(visited, graph, current_node):
    if current_node not in visited:
        print(current_node, end=" ")
        visited.add(current_node)

        for neighbour in graph[current_node]:
            dfs(visited, graph, neighbour)

print("Depth First Search:")
dfs(visited_dfs, graph_dfs, '1')  # Call function with starting node as '1'
