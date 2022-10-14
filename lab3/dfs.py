# DFS
# Using recursion


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def __str__(self):
        return self.graph

    def add_edge(self, e: int, v: int):
        self.graph[e].append(v)

    # Method to use in dfs()
    def dfs_util(self, v: int, visited: list):
        visited.append(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                # Input
                print(f"{v} {neighbor}")
                self.dfs_util(neighbor, visited)

    def dfs(self):
        # Using list instead of set(needed in output)
        visited = []

        for vertex in list(self.graph):  # Using list() in order to change dict size
            if vertex not in visited:
                self.dfs_util(vertex, visited)

        return visited
