# Design a class for all the Graph traversal types (BFS, DFS).

graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited =set() # list for visited nodes
queue = []  # initialise a queue 

def bfs(visited,graph,node):  # function for BFS

    visited.add(node)
    queue.append(node) 

    while queue:           # creating a loop to visit each node
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
          if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)


print("\nFollowing is the Breadth First Search")
bfs(visited,graph,'5')  

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
       

print("\nFollowing is the Depth First Search")
dfs(visited, graph, '5')
