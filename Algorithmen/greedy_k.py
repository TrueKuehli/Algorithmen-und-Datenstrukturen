from itertools import combinations

def getVal(item):
  """
  Get value of an item, as weight / value, used for sorting

  Args:
    item: A dictionary with entries "weight" and "value"

  Returns:
    The item's weight per value
  """
  return item["weight"] / item["value"]

def greedy0(items, limit, fixed_values):
  """
  Calculate lower bound for Maximum Knapsack, by using a similar
  algorithm to Greedy for Fractional Knapsack. This usually does not return
  the optimal value, but can be used as a lower bound.

  Args:
    items: An array of dictionarys with "weight" and "value" attributes
    limit: The limit or capacity of the Knapsack
    fixed_values: Predetermined values {0, 1} for items

  Returns:
    tuple: (value of chosen items, list of items)
  """
  sortedItems = sorted(items, key = getVal) # Sort items by weight/value asc.
  out = fixed_values.copy() # Initialize with fixed values

  # Initialze sums with fixed values
  currentSum = sum([0 if out[i] == None else items[i]["weight"] * out[i] for i in range(len(out))])
  currentVal = sum([0 if out[i] == None else items[i]["value"] * out[i] for i in range(len(out))])

  # Iterate through remaining items
  for i in range(len(sortedItems)):
    index = items.index(sortedItems[i]) # Find original index
    if out[index] != None:
      continue # If value was fixed, continue with next item
    if (currentSum + sortedItems[i]["weight"]) <= limit:
      # Item fits
      currentSum += sortedItems[i]["weight"]
      currentVal += sortedItems[i]["value"]
      out[index] = 1
    else:
      # Item doesn't fit
      out[index] = 0

  return (currentVal, out)

def greedy_k(items, limit, fixed_amount):
  """
  Approximates Greedy for Maximum Knapsack for up to fixed_amount fixed values

  Args:
    items: An array of dictionarys with "weight" and "value" attributes
    limit: The limit or capacity of the Knapsack
    fixed_amount: The maximum number of fixed values to check.

  Returns:
    tuple: (value of best solution that was found, best solution that was found)
  """
  # Best solution and current record
  g_k = 0
  best_solution = []

  # Fix 0 values, 1 value, ..., fixed_amount values
  for fixed_amount_smaller_equals in range(0, fixed_amount + 1):
    # Iterate through all combinations of fixed values for the given amount
    for k_subset in combinations([i for i in range(len(items))], fixed_amount_smaller_equals):
      # Currently chosen subset
      print("M = " + str([k + 1 for k in k_subset]))
      # Weight of fixed values
      print("sum(z_i) = " + str(sum([items[i]["weight"] for i in range(len(items)) if i in k_subset])))
      # Weight left for non-fixed items
      print("Z - sum(z_i) = " + str(limit - sum([items[i]["weight"] for i in range(len(items)) if i in k_subset])))
      # If solution not invalid (ie. not over the limit)
      if sum([items[i]["weight"] for i in range(len(items)) if i in k_subset]) <= limit:
        # Create new instance with fixed values "for free"
        new_items = [
          {'weight': items[i]['weight'] * (0 if i in k_subset else 1),
           'value': items[i]['value']}
          for i in range(len(items))]
        # and set new limit for instance to the remaining space in knapsack
        new_limit = limit - sum([items[i]["weight"] for i in range(len(items)) if i in k_subset])

        # Run Greedy0 on new instance
        (g_solution, solution) = greedy0(new_items, new_limit, [None for i in range(len(items))])
        # Greedy0 solution
        print("G = " + str(g_solution))

        # Save if new record
        if g_solution > g_k:
          g_k = g_solution
          best_solution = solution

      # Current record and it's solution
      print("G_k = " + str(g_k))
      print("S = " + str([i + 1 for i in range(len(best_solution)) if best_solution[i] == 1]))
      print()
  return (best_solution, g_k)



items = [
  {'weight': 18, 'value': 19},
  {'weight': 20, 'value': 20},
  {'weight': 22, 'value': 21},
  {'weight': 19, 'value': 16},
]
limit = 41
fixed_amount = 2

print(greedy_k(items, limit, fixed_amount))
