from boyer_moore import search


def main():
    # Average case
    text = "ABAAABCD"
    pattern = "ABC"

    # Best case: all letters in pattern and text are different. Time complexity of algorithm: O(n/m)
    # text = "ABCDEFGH"
    # pattern = "DEF"

    # Worst case: all letters in pattern and text are the same. Time complexity of algorithm: O(n*m)
    # text = "AAAAAAAA"
    # pattern = "AAA"

    search(text, pattern)


if __name__ == "__main__":
    main()
