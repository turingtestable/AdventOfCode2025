def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
    data =[]
    for line in lines:
      char_list = list(line)
      data.append(list(map(int,char_list)))
    return data

def sum_charges(data):
  total = 0
  for line in data:
    total += find_charge(line)
  return total

def find_charge(line):
  first_digit = max(line[0:len(line) - 1])
  second_digit = max(line[line.index(first_digit) + 1:])
  return int(str(first_digit)+str(second_digit))

def sum_overcharges(data):
  total = 0
  for line in data:
    total += find_overcharge(line)
  return total

def find_overcharge(line):
  digit_index = 0
  distance_from_end = 11
  digits = ""
  while len(digits) < 12:
    if (distance_from_end == 0):
      current_digit = max(line[digit_index:])
    else:
      current_digit = max(line[digit_index:len(line)-distance_from_end])
    digit_index = line[digit_index:].index(current_digit) + digit_index + 1
    distance_from_end += -1
    digits = "".join([digits,str(current_digit)])
  return int(digits)

def main():
  data = import_data()
  print("Part 1:")
  print(sum_charges(data))
  print("Part 2:")
  print(sum_overcharges(data))

main()