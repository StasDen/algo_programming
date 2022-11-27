# Boyer Moore algorithm for patter searching
# Done via: https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/


NO_0F_CHARS = 256


def bad_char_heuristic(string: str, size: int):
    bad_char = [-1] * NO_0F_CHARS

    for i in range(size):
        bad_char[ord(string[i])] = i
    return bad_char


def search(text: str, pattern: str):
    n = len(text)
    m = len(pattern)

    bad_char = bad_char_heuristic(pattern, m)

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print(f"Pattern occurred at shift: {s}")

            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
