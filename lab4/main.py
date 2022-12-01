from electricians import find_longest_wire


def main():
    # Test1
    # max_length = find_longest_wire(None, [2, 5, 7])

    # Test2
    max_length = find_longest_wire(100, [1, 1, 1])

    # Test3
    # max_length = find_longest_wire(2, [3, 1, 3])

    # Test4
    # max_length = find_longest_wire(4, [100, 2, 100, 2, 100])

    print(f"The longest wire is {max_length}")


if __name__ == '__main__':
    main()
