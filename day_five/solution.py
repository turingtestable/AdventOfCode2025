fresh_ranges = []

def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
    fresh_ranges = []
    ingredient_ids = []
    for line in lines:
      if line.find("-") > -1:
        fresh_ranges.append(line)
      elif line.isdigit():
        ingredient_ids.append(int(line))
    return [fresh_ranges, ingredient_ids]

def count_fresh(data):
  count = 0
  fresh_ranges_string = data[0]
  ingredient_ids = data[1]
  fresh_set = set()
  for span in fresh_ranges_string:
    bounds = span.split("-")
    fresh_ranges.append([int(bounds[0]), int(bounds[1])])
  for ingredient_id in ingredient_ids:
    if check_id_freshness(ingredient_id, fresh_ranges):
      count += 1
  return count

def check_id_freshness(id, ranges):
  for span in ranges:
    if span[0]<= id and span[1]>= id:
      return True
  return False

def count_all_fresh():
  global fresh_ranges
  fresh_ranges.sort()
  i = 0
  final_ranges = []
  while i < len(fresh_ranges) - 1:
    if fresh_ranges[i][1] > fresh_ranges[i+1][0]:
      if i+2 < len(fresh_ranges):
        fresh_ranges = fresh_ranges[0:i] + [[fresh_ranges[i][0], fresh_ranges[i+1][1]]] + fresh_ranges[i+2:]
      else:
        fresh_ranges = fresh_ranges[0:i] + [[fresh_ranges[i][0], fresh_ranges[i+1][1]]]
    else:
      i+=1
  count = 0
  for span in fresh_ranges:
    count += span[1] - span[0] + 1
  return count

def main():
  data = import_data()
  print("Part 1:")
  print(count_fresh(data))
  print("Part 2:")
  print(count_all_fresh())

main()