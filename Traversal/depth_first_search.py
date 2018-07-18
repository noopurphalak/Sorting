graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
    print(str(visited))


def dfs1(graph, start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for next in graph[start] - set(visited):
            dfs1(graph, next, visited)
    return visited


if __name__ == "__main__":
    dfs(graph, 'A')
    print(dfs1(graph, 'A'))
