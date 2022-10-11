# Cartesian product


# Counter
cnt = 0


def cart_product(arr1: list, arr2: list, arr1_size: int, arr2_size: int):
    # Using global var
    global cnt

    for i in range(0, arr1_size):
        for j in range(0, arr2_size):

            # Printing pairs like 2: 3
            if (arr1[i] % 2) == 0 and (arr2[j] % 2) != 0:
                print(f"{arr1[i]}: {arr2[j]}")
                cnt += 1

            # Printing pairs like 2: 3
            elif (arr1[i] % 2) != 0 and (arr2[j] % 2) == 0:
                print(f"{arr1[i]}: {arr2[j]}")
                cnt += 1

    print(f"Number of couples: {cnt}")
