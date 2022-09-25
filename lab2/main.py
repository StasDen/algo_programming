from graph_root_vertex import find_root, write_in_input, write_in_output


def main():
    # Graph with only one root
    graph1 = {
        1: [2, 3],
        2: [4, 5],
        3: [4, 7],
        4: [6],
        5: [],
        6: [5],
        7: [6]
    }

    # Graph with many roots(returning one of them)
    graph2 = {
        0: [1],
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: [0]
    }

    # Graph without root
    graph3 = {
        0: [1],
        1: [],
        2: [1]
    }

    # Empty graph
    graph4 = {}

    write_in_input(graph1)
    result = find_root()
    write_in_output(result)


if __name__ == '__main__':
    main()
