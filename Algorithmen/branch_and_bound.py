import math

def getVal(item):
  """
  Get value of an item, as weight / value, used for sorting

  Args:
    item: A dictionary with entries "weight" and "value"

  Returns:
    The item's weight per value
  """
  return item["weight"] / item["value"]

def greedy(items, limit, fixed_values):
  """
  Calculate solution to Fractional Knapsack via Greedy-Algorithm
  Used as an upper bound for Maximum Knapsack

  Args:
    items: An array of dictionarys with "weight" and "value" attributes
    limit: The limit or capacity of the Knapsack
    fixed_values: Predetermined values [0, 1] for items

  Returns:
    The optimal value for the Fractional Knapsack instance
  """
  sortedItems = sorted(items, key = getVal) # Sort items by weight/value asc.

  out = fixed_values.copy() # Initialize with fixed values

  # Initialze sums with fixed values
  currentSum = sum([0 if out[i] == None else items[i]["weight"] * out[i] for i in range(len(out))])
  currentVal = sum([0 if out[i] == None else items[i]["value"] * out[i] for i in range(len(out))])

  # Iterate through remaining objects
  for i in range(len(sortedItems)):
    index = items.index(sortedItems[i]) # Find original index
    if out[index] != None:
      continue # If value was fixed, continue with next item
    if (currentSum + sortedItems[i]["weight"]) <= limit:
      # Item fits in completely
      currentSum += sortedItems[i]["weight"]
      currentVal += sortedItems[i]["value"]
      out[index] = 1
    else:
      # Item fits in partially, in proportial of x (can be 0)
      x = (limit - currentSum) / sortedItems[i]["weight"]
      currentSum += x * sortedItems[i]["weight"]
      currentVal += x * sortedItems[i]["value"]
      out[index] = x

  return currentVal # Optimal value for Fractional Knapsack

# Maximum Knapsack; Lower Bound
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
    Lower bound value for Maximum Knapsack
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

  return currentVal

def branch_and_bound(items, capacity, current_solution, branch_index, fixed_values):
  print()
  print(branch_index)
  print(fixed_values)
  if sum([0 if fixed_values[i] == None else fixed_values[i] * items[i]["weight"] for i in range(branch_index)], 0) > capacity:
    print("Invalid configuration")
    return current_solution # Invalid, capacity overloaded
  lower_bound = greedy0(items, capacity, fixed_values) # Calculate Lower Bound
  print("P = " + str(lower_bound))
  if lower_bound > current_solution:
    current_solution = lower_bound # Improve solution
  if branch_index >= len(items):
    print("Leaf reached")
    return current_solution # Reached Leaf

  # Caulculate Upper Bound
  upper_bound = math.floor(greedy(items, capacity, fixed_values))
  print("U = " + str(upper_bound))

  # If the upper bound with the currently fixed values is less than the current
  # optimal value, we don't need to continue with the current fixed values
  if upper_bound > current_solution:
    fxd_values = fixed_values.copy()
    fxd_values[branch_index] = 0
    sub_solution = branch_and_bound(items, capacity, current_solution, branch_index + 1, fxd_values) # Calculate sub-solution, fixing current item to 0
    if sub_solution > current_solution:
      # Sub-routine found better solution
      current_solution = sub_solution
    fxd_values[branch_index] = 1
    sub_solution = branch_and_bound(items, capacity, current_solution, branch_index + 1, fxd_values) # Calculate sub-solution, fixing current item to 1
    if sub_solution > current_solution:
      # Sub-routine found better solution
      current_solution = sub_solution

  return current_solution

items = [
  {'weight': 24, 'value': 25},
  {'weight': 28, 'value': 28},
  {'weight': 12, 'value': 11},
  {'weight': 18, 'value': 16},
]
capacity = 42
current_solution = 0
branch_index = 0
fixed_values = [
  None,
  None,
  None,
  None,
]

print(branch_and_bound(items, capacity, current_solution, branch_index, fixed_values))
