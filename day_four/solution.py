def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
    data = []
    for line in lines:
      data.append(list(line))
    return data

def check_location(data, location):
  rolls = 0
  x = location[0] - 1
  y = location[1] - 1
  while x < (location[0] + 2):
    while y < (location[1] + 2):
      if (
            [location[0],location[1]] != [x,y] and x >= 0 and y >= 0 and
            x < len(data) and y < len(data[location[0]]) and
            data[x][y] == "@"
        ):
          rolls += 1
      y += 1
    x += 1
    y = location[1] - 1
  if rolls >=4:
    return False
  return True

def count_rolls(data, total_rolls):
  location = [0,0]
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data[i][j] == "@" and check_location(data, [i,j]):
        total_rolls.append([i,j])
  return total_rolls

def count_rolls_until_no_change(data):
  total_rolls = []
  current_rolls = -1
  while len(total_rolls) != current_rolls:
    current_rolls = len(total_rolls)
    total_rolls = count_rolls(data, total_rolls)
    data = remove_rolls(data, total_rolls)
  return total_rolls

def remove_rolls(data, total_rolls):
  for roll in total_rolls:
    data[roll[0]][roll[1]] = "."
  return data

def main():
  data = import_data()
  print("Part 1:")
  print(len(count_rolls(data, [])))
  print("Part 2:")
  print(len(count_rolls_until_no_change(data)))


main()