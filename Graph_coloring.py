 #graph coloring
def isSafe(graph, color):
 
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if (graph[i][j] and color[j] == color[i]):
                return False
    return True
  
def graphColoring(graph, board, i, color):    
 
    if (i == 4):
 
        if (isSafe(graph, color)):
 
            printSolution(color)
            return True
        return False
 
    for j in range(1, board + 1):
        color[i] = j
 
        if (graphColoring(graph, board, i + 1, color)):
            return True
        color[i] = 0
    return False
  
def printSolution(color):
    print("Solution Exists:" " Following are the assigned colors ")
    for i in range(len(graph)):
        print(color[i], end=" ")
 
if __name__ == '__main__':
 
    graph = [
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 0, 0],
    ]
    m = 3                                    # Number of colors
 
    color = [0 for i in range(len(graph))]    # Function call
 
    if (not graphColoring(graph, m, 0, color)):
        print("Solution does not exist")
 
    
