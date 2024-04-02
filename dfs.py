def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited



graph = {'0': set(['2']),
         '1': set(['3']),
         '2': set(['0'])}


dfs(graph, '0')