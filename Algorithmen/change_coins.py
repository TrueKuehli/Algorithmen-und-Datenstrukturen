def give_change(change_total):
  """
  Simple greedy algorithm for calculating minimum coins
  needed to output change

  Uses coins:
    200ct
    100ct
    50ct
    20ct
    10ct
    5ct
    2ct
    1ct

  This does not work with any type of coin system. For
  instance extend the upper example with a 4ct coin.
  Input = 8; results in 5ct + 2ct + 1ct
  However, 4ct + 4ct would be the optimal result.
  With the example coin system used, the greedy algo will
  always give the correct answer however.
  """
  change_coins = []
  for i in [200, 100, 50, 20, 10, 5, 2, 1]:
    while change_total - i >= 0:
      change_total -= i
      change_coins.append(i)
  return change_coins

print(give_change(1231));
