# Task: find possible couples between two tribes
#
# 1) Girls are even num, boys are odd
# 2) Each row - new tribe(graph)
# For example,
# Input:
# 1 2
# 2 4
# 3 5
# In first tribe there are two girls(2, 4) and a boy(1); in second two boys(3, 5). Number of rows: 3
#
# Using DFS, cartesian product


from cart_prod import cart_product


def find_couples(row_num: int, graph1, graph2):
    print(f"Number of inputted rows: {row_num}")

    # DFS
    print("Input:")
    arr1 = graph1.dfs()
    arr2 = graph2.dfs()

    # Cart product
    print("Couples:")
    l1 = len(arr1)
    l2 = len(arr2)
    cart_product(arr1, arr2, l1, l2)
