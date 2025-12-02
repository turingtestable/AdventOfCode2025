def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
    ranges = []
    for line in lines:
        for range in line.split(","):
            ranges.append(range.split("-"))
    return ranges

def check_double(number):
    number_str = str(number)
    half = int(len(number_str)/2)
    if len(number_str)%2 != 0:
        return False
    elif number_str[0:half] == number_str[half::]:
        return True
    else:
        return False

def check_repeats(number):
    number_str = str(number)
    length = len(number_str)
    for i in range(1, length):
        if length%i == 0:
            str_slice = number_str[0:i]
            remainder = number_str[i:]
            value = True
            while len(remainder) > 0:
                if str_slice == remainder[0:i]:
                    remainder = remainder[i:]
                else:
                    value = False
                    break
            if value:
                return True
    return False


def calculate_double_values(data):
    running_total = 0
    for datum in data:
        i = int(datum[0])
        while i <= int(datum[1]):
            if check_double(i):
                running_total += i
            i+=1
    return running_total

def calculate_any_repeats_values(data):
    running_total = 0
    for datum in data:
        i = int(datum[0])
        while i <= int(datum[1]):
            if check_repeats(i):
                running_total += i
            i+=1
    return running_total


def main():
    data = import_data()
    print("Part 1:")
    print(str(calculate_double_values(data)))
    print("Part 2:")
    print(str(calculate_any_repeats_values(data)))

main()