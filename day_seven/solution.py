from collections import defaultdict

def import_data():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        return(list(map(list, lines)))

def split_lines(data):
    x_s = set()
    x_s.add(data[0].index("S"))
    y = 0
    split_count = 0
    while y < len(data):
        new_x_s = set()
        for x in x_s:
            if data[y][x] == "^":
                new_x_s.add(x-1)
                new_x_s.add(x+1)
                split_count += 1
            else:
                new_x_s.add(x)
        x_s = new_x_s
        y+=1
    return split_count

def split_time_lines(data):
    time_lines = defaultdict(int)
    time_lines[data[0].index("S")] += 1
    y = 0
    while y < len(data):
        print(y)
        new_time_lines = defaultdict(int)
        for x in time_lines.keys():
            if data[y][x] == "^":
                new_time_lines[x+1] += time_lines[x]
                new_time_lines[x-1] += time_lines[x]
            else:
                new_time_lines[x] += time_lines[x]
        time_lines = new_time_lines
        y+=1
    counter = 0
    for value in time_lines.values():
        counter += value
    return(counter)        

def main():
    data = import_data()
    print(split_lines(data))
    print(split_time_lines(data))

main()