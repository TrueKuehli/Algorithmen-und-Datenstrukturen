def maximum_knapsack(items, limit):
  """
  Berechnet die Lösung für Maximum Knapsack über Dynamic Programming
  (ähnlich wie Subset Sum)
  """
  # Erstelle Tabelle
  table = [[None for j in range(len(items) + 1)] for i in range(limit + 1)]
  
  # Fülle erste Zeile mit 0 (da der Wert im Knapsack mit 0 Gegenständen immer 0 ist)
  for x in range(limit + 1):
    table[x][0] = 0
  
  # Füge immer mehr Gegenstände hinzu
  for i in range(1, len(items) + 1):
    # Fülle bis zum Gewicht des neuen Gegenstandes die Tabelle mit der vorherigen Zeile
    for x in range(items[i - 1]["weight"]):
      table[x][i] = table[x][i - 1]
    
    # Fülle
    for x in range(items[i - 1]["weight"], limit + 1):
      # Wenn der Wert "Gewicht"-Spalten vorher + der Wert des momentanen Gegenstandes
      # größer ist, als der Wert der Zeile drüber, dann ist füge den ersteren Wert ein
      # (Wir schauen also, ob irgendein leichterer Rucksack plus das aktuelle Element
      # besser ist, als irgendein anderer Rucksack, der genau so viel wiegt, wie ersterer)
      if (table[x - items[i - 1]["weight"]][i - 1] + items[i - 1]["value"]) > table[x][i - 1]:
        table[x][i] = table[x - items[i - 1]["weight"]][i - 1] + items[i - 1]["value"]
      else:
        # Ansonsten übernehmen wir die Zeile drüber, da es scheinbar besser ist, das
        # aktuelle Element NICHT zu wählen.
        table[x][i] = table[x][i - 1]
  print_table(table) # Zeige die Tabelle im Terminal

  return table[limit][len(items)] # Gib den optimalen Wert von Maximum Knapsack zurück

def print_table(two_arr):
  """
  Helper-Funktion zur Ausgabe der Tabelle
  
  Args:
    two_arr: 2-dimensionaler Array, als Array von Spalten
  """
  for y in range(len(two_arr[0])):
    for x in range(len(two_arr)):
      print(two_arr[x][y], end="\t")
    print()

items = [
  {"weight": 5, "value": 1},
  {"weight": 4, "value": 3},
  {"weight": 3, "value": 1},
  {"weight": 5, "value": 2},
  {"weight": 6, "value": 4},
]
limit = 11

print(maximum_knapsack(items, limit))
