def dfs(graph, start, length, visited=None):

    try:
        if visited is None:
            visited = set()
        visited.add(start)
    except Exception as err:
        print ("The node is not valid" + start)
        raise err

    print("Start at ", start)

    print("Length is ", length)

    for next in graph[start] - visited:
        dfs(graph, next, length + 1, visited)
    return visited


graph = {
    '0': set(['2']),
    '1': set(['3']),
    '2': set(['0']),
    '3': set(['1'])
    }


ln = 0

dfs(graph, '7', ln)
