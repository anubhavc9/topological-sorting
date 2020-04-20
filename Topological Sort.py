# finding the in-degree of each vertex
def findInDegree(adjMatrix):
    indegree = []
    for j in range(0, len(adjMatrix[0])):
        tmp = 0
        for i in range(0, len(adjMatrix)):
            tmp = tmp + adjMatrix[i][j]
        indegree.append(tmp)
    return indegree

print("NOTE: If there's an edge from i to j, adjmat[i][j] = 1. Else, adjmat[i][j] = 0")
n = int(input("Enter the number of vertices in the directed acyclic graph (DAG): "))
adjMatrix = []
vertex = []
topologicalOrder = []
# taking input
for i in range(0, n):
    print("Enter row {} of the adjacency matrix".format(i+1))
    for j in range(0, n):
        v = int(input())
        vertex.append(v)
    adjMatrix.append(vertex)
    vertex = []

print("The adjacency matrix is {}".format(adjMatrix))

# finding the topological order
for x in range(0, n):
    result = findInDegree(adjMatrix)
    minIndex = result.index(min(result))
    topologicalOrder.append(minIndex+1)
    count = 0
    for i in adjMatrix:
        i[minIndex] = 999
    for x in adjMatrix[minIndex]:
        adjMatrix[minIndex][count] = 999
        count += 1

print("One of the valid topological orders is {}".format(topologicalOrder))