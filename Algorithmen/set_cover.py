def argmax_sets(elements, intersect_with):
  maximum = 0
  argmax = set()
  for i in range(len(elements)):
    s = elements[i]
    if len(s.intersection(intersect_with)) > maximum:
      argmax = s
  return argmax
    

def greedy_set_cover(universe, sets):
  covered = set()
  to_cover = universe.copy()
  set_cover = []
  costs = {}
  
  while covered != universe:
    greedy_set = argmax_sets(sets, to_cover)
    intersected_set = greedy_set.intersection(to_cover)
    set_cardinality = len(intersected_set)
    
    cost = 1 / set_cardinality
    for s in intersected_set:
      costs[str(s)] = cost
    
    covered = covered.union(greedy_set)
    to_cover = to_cover.difference(greedy_set)
    set_cover.append(greedy_set)
    
    print(greedy_set)
    print(cost)
    print(covered)
    print(to_cover)
    print()
  
  print(costs)
  print()
  return set_cover

universe = set([i for i in range(1, 11)])
sets = [
  set([1,2,3,7,9]),
  set([4,5,6,8,10]),
  set([1,2,3,4,5,6]),
  set([7,8]),
  set([9,10])
]
print(greedy_set_cover(universe, sets))