from dfs import Graph
from find_couples import find_couples


def main():
    # Splitting one graph to two equal ones
    # One graph(ex1)
    g1 = Graph()
    g1.add_edge(1, 2)
    g1.add_edge(2, 4)
    g1.add_edge(3, 5)

    # Two equal graphs
    g1_1 = Graph()
    g1_1.add_edge(1, 2)
    g1_1.add_edge(2, 4)
    g1_2 = Graph()
    g1_2.add_edge(3, 5)

    # One graph(ex2)
    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 4)
    g2.add_edge(3, 5)
    g2.add_edge(8, 10)

    # Two equal graphs
    g2_1 = Graph()
    g2_1.add_edge(1, 2)
    g2_1.add_edge(1, 3)
    g2_1.add_edge(2, 4)
    g2_1.add_edge(3, 5)
    g2_2 = Graph()
    g2_2.add_edge(8, 10)

    # One graph(ex3)
    g3 = Graph()
    g3.add_edge(5, 6)
    g3.add_edge(6, 7)
    g3.add_edge(8, 10)
    g3.add_edge(10, 11)

    # Two equal graphs
    g3_1 = Graph()
    g3_1.add_edge(5, 6)
    g3_1.add_edge(6, 7)
    g3_2 = Graph()
    g3_2.add_edge(8, 10)
    g3_2.add_edge(10, 11)

    find_couples(3, g1_1, g1_2)


if __name__ == '__main__':
    main()
