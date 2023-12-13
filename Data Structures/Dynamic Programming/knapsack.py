# Knapsack
# # with max weight of 165, get the most value in the knapsack

weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
values = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
capacity = 165

# Knapsack (Recursive, Static)
def knapsack_recursive(W, V, c, current_item):
    pass


print(knapsack_recursive(weights, values, capacity, len(values)-1))


# Knapsack (Dynamic, Memoization)
def knapsack_adv(W, V, C):
    pass


# helper, main knapsack function
def knapsack_adv_helper(W, V, C, n, M):
    pass


# Knapsack (Dynamic, Space Optimized)
# W= array of weights, V= array of values, C= total capacity
def knapsack_memoization(W, V, C):
    pass


# knapsack dynamic helper function
def dyn_helper(W, V, C, n, M):
    pass


# driver code
W = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
V = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
C = 165

print (knapsack_adv(W, V, C))