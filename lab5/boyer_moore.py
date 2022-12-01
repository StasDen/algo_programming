# Boyer Moore algorithm for pattern searching
# Done via: https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/


NO_0F_CHARS: int = 256  # Using "256" to cover all alphabet characters


# Func to use in search for better performance
def bad_char_heuristic(string: str, size: int):
    # Default list
    bad_char = [-1] * NO_0F_CHARS

    # Filling list with actual values of occurrences and returning it
    for i in range(size):
        bad_char[ord(string[i])] = i
    return bad_char


# Main func
def search(text: str, pattern: str):
    n = len(text)
    m = len(pattern)

    # Executing func for our pattern
    bad_char = bad_char_heuristic(pattern, m)

    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print()

    s = 0  # "s" means shift(position)

    # Executing "while" until all pattern occurrences will be found
    while s <= n - m:

        j = m - 1  # Starting from "0"

        # When finding pattern letters in text - decreasing "j". Starting search from the end
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # When j < 0 - pattern is found
        if j < 0:
            print(f"Pattern occurred at position: {s}")

            # Using heuristic list to find other occurrences of pattern in text
            if s + m < n:
                s += m - bad_char[ord(text[s + m])]

            # If there isn't letter in list - moving one character at time
            else:
                s += 1
        else:
            # When still searching - using heuristic list to quickly find new pattern letters
            s += max(1, j - bad_char[ord(text[s + j])])
