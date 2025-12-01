def import_data():
  with open("input.txt") as file:
    return file.read().splitlines()

def count_zeroes(instruction_list):
  positions = list(range(100))
  current_index = 50
  zero_count = 0
  for line in instruction_list:
    if line[0] == "L":
      new_index = current_index - int(line[1:])%100
      current_index = positions[new_index]
    else:
      current_index = (current_index + int(line[1:])) % 100
    if current_index == 0:
      zero_count += 1
  return zero_count

def count_click_zeroes(instruction_list):
  positions = list(range(100))
  current_index = 50
  zero_count = 0
  for line in instruction_list:
    prev_index = current_index
    instruction = int(line[1:])
    zero_count += instruction // 100
    if line[0] == "L":
      current_index = positions[current_index - instruction%100]
    else:
      current_index = (current_index + instruction)%100
    if current_index == 0:
      zero_count += 1
    elif line[0] == "L" and prev_index < current_index and prev_index != 0:
      zero_count += 1
    elif line[0] == "R" and prev_index > current_index and prev_index !=0:
      zero_count += 1
  return zero_count

def main():
  data = import_data()
  print("Part 1:")
  print(count_zeroes(data))
  print("Part 2:")
  print(count_click_zeroes(data))
main()