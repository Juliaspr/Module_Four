import collections


def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print(visited)


if name == 'main':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]}
    bfs(graph, 0)


