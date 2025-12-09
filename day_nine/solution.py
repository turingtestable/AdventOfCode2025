from collections import defaultdict

max_x_s = defaultdict(int)
min_x_s = {}
max_y_s = defaultdict(int)
min_y_s = {}

def import_data():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        data = []
        for line in lines:
            list_list = line.split(",")
            data.append(list(map(int, list_list)))
        return data

def calculate_max_rectangle(data):
    current_max = 0
    for i in range(len(data)):
        for j in range(len(data)):
            current_area = area(data[i], data[j])
            current_max = max(current_max, current_area)
    return current_max

def area(coor_1, coor_2):
    return (abs(coor_1[0] - coor_2[0])+1) * (abs(coor_1[1] - coor_2[1]) +1)

def is_only_rg(coor1, coor2):
    if (within_bounds([coor1[0], coor2[1]]) 
        and within_bounds([coor2[0], coor1[1]]) 
        and within_bounds(coor1) 
        and within_bounds(coor2)):
        x_s = [coor1[0], coor2[0]]
        y_s = [coor1[1], coor2[1]]
        x_s.sort()
        y_s.sort()
        x = x_s[0]
        while x <= x_s[1]:
            if (not (within_bounds([x,y_s[0]]) and within_bounds([x,y_s[1]]))):
                return False
            x+=1
        y = y_s[0]
        while y <= y_s[1]:
            if (not (within_bounds([x_s[0],y]) and within_bounds([x_s[1],y]))):
                return False
            y+=1
        return True
    return False

def within_bounds(coor):
    global max_x_s
    global min_x_s
    return (
            coor[0] in min_x_s.keys() and min_x_s[coor[0]] <= coor[1] and max_x_s[coor[0]] >= coor[1] 
            and coor[1] in min_y_s.keys() and min_y_s[coor[1]] <= coor[0] and max_y_s[coor[1]] >= coor[0]
    )

def calculate_max_interior_rectangle(data):
    current_max = 0
    rg_data = build_rg_data(data)
    counter = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i < j:
                print(format(counter/(len(data)**2/2), '.2%'))
                counter += 1
                current_area = area(data[i], data[j])
                if current_area > current_max and is_only_rg(data[i], data[j]):
                    current_max = current_area
                    print(current_max)
    return current_max

def update_min_max(coor):
    global max_x_s
    global min_x_s
    global max_y_s
    global min_y_s
    max_x_s[coor[0]] = max(max_x_s[coor[0]], coor[1])
    max_y_s[coor[1]] = max(max_y_s[coor[1]], coor[0])
    if coor[0] in min_x_s.keys():
        min_x_s[coor[0]] = min(min_x_s[coor[0]], coor[1])
    else:
        min_x_s[coor[0]] = coor[1]
    if coor[1] in min_y_s.keys():
        min_y_s[coor[1]] = min(min_y_s[coor[1]], coor[0])
    else:
        min_y_s[coor[1]] = coor[0]

def build_rg_data(data):
    rg_data = []
    global max_x_s
    global min_x_s
    global max_y_s
    global min_y_s
    for i in range(len(data)):
        update_min_max(data[i])
        if i == 0:
            j = len(data)-1
        else:
            j = i - 1
        rg_data.append(data[i])
        rg_data.append(data[j])
        if data[i][0] == data[j][0]:
            if data[j][1] < data[i][1]:
                i , j = j, i
            current = data[i][1] +1
            while current < data[j][1]:
                update_min_max([data[i][0], current])
                rg_data.append([data[i][0], current])
                current += 1
        else:
            if data[j][0] < data[i][0]:
                i , j = j , i
            current = data[i][0] + 1
            while current < data[j][0]:
                update_min_max([current, data[i][1]])
                rg_data.append([current, data[i][1]])
                current += 1
    # print(min_x_s)
    # print(dict(max_x_s))
    return rg_data

def main():
    data = import_data()
    print("Part 1:")
    print(calculate_max_rectangle(data))
    print("Part 2:")
    print(calculate_max_interior_rectangle(data))


main()
