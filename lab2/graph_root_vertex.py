# Finding root(mother) vertex of directed graph
# Using BFS

import collections


def find_root():
    c = 0  # Counter
    i = 0  # Iterator

    # Getting info from input
    input_file = open("input.txt", "r")
    graph_str = input_file.read()
    graph_dict = eval(graph_str)  # Creating dict from str

    if graph_dict is not None:
        root = -1  # Default val

        if i < len(graph_dict):
            visited, queue = set(), collections.deque([list(graph_dict)[i]])
            visited.add(list(graph_dict)[i])

            while queue:
                c += 1

                v = queue.popleft()
                print(str(v) + " ", end="")

                # If not visited
                for neighbor in graph_dict[v]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

                if c == len(graph_dict):
                    root = list(graph_dict)[i]

                    print()
                    print(f"{root} is root")

            i += 1

            if root == -1:
                print()
                print("No root")

            return root  # Returning -1 if no root


# Input
def write_in_input(graph: dict):
    input_file = open("input.txt", "w")
    input_file.write(str(graph))
    input_file.close()


# Output
def write_in_output(result: int):
    output_file = open("output.txt", "w")
    output_file.write(str(result))
    output_file.close()
