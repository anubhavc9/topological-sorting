# topological-sorting

A topological sort or topological ordering of a directed acyclic graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG). Based on different criteria, there can be multiple topological orderings possible for a single DAG. This program finds the fewest edges first topological order.

# Applications of Topological Sorting
• Representing course prerequisites
• Detecting deadlocks
• Pipeline of computing jobs
• Checking for symbolic link loop
• Evaluating formulae in spreadsheet

# How to use
Enter the number of vertices in the graph
Enter the row-wise adjacency matrix for the graph, with each number on a line
If there is a directed edge from vertex 1 to vertex 2, adjmatrix[1][2] = 1
If there is no directed edge from vertex 1 to vertex 2, adjmatrix[1][2] = 0
