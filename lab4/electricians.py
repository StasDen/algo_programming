# Task: electricians
# Finding the longest wire between pillars
# "w" - distance between two neighbor pillars, "heights" - list of pillars heights


from math import sqrt
from itertools import permutations


def find_longest_wire(w: int, heights: list[int]):
    # If one of the params is "None" - leaving the func
    if w is None or heights is None:
        print("Set 'w' and 'heights' parameters")
        return

    # If params are well set - executing
    else:
        counter: float = 0
        possible_lengths = []

        # Using built-in func to find all "heights" permutations
        pillars_permutations_list = list(permutations(heights))
        print(f"All pillars permutations: {pillars_permutations_list}")
        print()

        for arr in pillars_permutations_list:
            # We need not last, but second last el in arr - using "len(arr) - 1"
            for i in range(len(arr) - 1):
                # Avoiding index out of bounds error
                if (i + 1) != len(arr):
                    # If heights with the same length, wire length - distance between pillars
                    if arr[i] == arr[i + 1]:
                        wire_length_between_two_neighbor_pillars = w

                    # If heights are different - using Pythagorean theorem to find hypotenuse
                    else:
                        wire_length_between_two_neighbor_pillars = sqrt((arr[i] - arr[i + 1]) ** 2 + w ** 2)

                    # Finding total
                    counter += wire_length_between_two_neighbor_pillars

            # We need two digits after comma - using built-in "round()"
            result = round(counter, 2)
            print(f"Wire length of {arr}: {result}")

            # Adding val to the list with possible lengths, so then to find max one
            possible_lengths.append(result)

            # Resetting counter to start with new arr
            counter = 0

        print()
        print(f"All wire lengths: {possible_lengths}")
        return max(possible_lengths)
