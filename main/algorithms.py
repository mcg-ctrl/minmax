from .models import FoodItem


def minmax_algo(min_option, min_cap, max_option, context):
    # A dictionary to track which items were used in the solution
    sol_dict = {}

    num_items = context.count()

    # 1-dimensional lists to store values, and weights for each item
    v = [0 for _ in range(0, num_items + 1)]
    w = [0 for _ in range(0, num_items + 1)]
    item_name = [0 for _ in range(0, num_items + 1)]

    # Loop through FoodItems and initialize the output dictionary
    # with the name and quantity set to zero
    j = 1
    for fooditem in context:

        # Fooditem and options tracking
        sol_dict[fooditem.name] = 0

        item_name[j] = fooditem.name

        # Determine "values" and "weights" of each item depending on the options
        # selected by the user in MinMaxForm. Needed for the knapsack solution
        if min_option == 'price':
            w[j] = int(fooditem.price * 100)  # Handles in terms of "cent" units
            if j == 1:
                min_cap = min_cap * 100
        if min_option == 'calories':
            w[j] = int(fooditem.calories)
        if max_option == 'protein':
            v[j] = int(fooditem.protein)
        if max_option == 'fiber':
            v[j] = int(fooditem.fiber)

        j += 1

    # Boundaries for the knapsack solution table
    n, B = num_items, min_cap

    # Knapsack table
    K = [[0 for _ in range(0, B + 1)] for _ in range(0, n + 1)]

    for i in range(1, n + 1):
        for b in range(1, B + 1):
            if w[i] <= b:
                # Pseudocode: K(i, b) = max{ v_i + K(i-1, b-w_i), K(i-1, b) }
                K[i][b] = max(v[i] + K[i - 1][b - w[i]], K[i - 1][b])
            else:
                # Pseudocode: K(i, b) = K(i-1, b)
                K[i][b] = K[i - 1][b]

    sol_val = K[n][B]

    # Backtracking to retrieve items used for the solution
    temp_sol_val = sol_val
    for k in range(n+1, 0, -1):
        # Variable to hold the value of the solution that has not been accounted for
        if temp_sol_val <= 0:
            # No solution was found
            break

        if temp_sol_val == K[k-1][B]:
            # This item was not used in the solution
            continue

        else:
            # This item was used in the solution
            # Increment item's value in the sol_dict
            sol_dict[item_name[k]] = sol_dict[item_name[k]] + 1
            temp_sol_val = temp_sol_val - v[k-1]

    # test

    return sol_dict, sol_val
