from functools import reduce


def import_data():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        data = []
        for line in lines:
            line_list = list(line)
            actual_list = []
            current_string = ""
            for i in range(len(line_list)):
                if line_list[i] == " " or i == len(line_list) - 1:
                    if line_list[i]!= " ":
                        current_string = int(current_string + line_list[i])
                        actual_list.append(current_string)
                        current_string = ""
                    elif len(current_string) != 0:
                        actual_list.append(current_string)
                        current_string = ""
                else:
                    current_string += line_list[i]
            data = data + [actual_list]
        return data

def import_data_other():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        data = list(map(lambda line: list(reversed(list(line))), lines))
    return data


def do_the_math(data):
    overall_total = 0
    for i in range(len(data[0])):
        current_total = 0 
        for j in range(len(data)-1):
            if current_total == 0: 
                current_total = data[j][i]
            else:
                if i >= len(data[j]):
                    print(data[j])
                expression = f"{current_total}{data[-1][i]}{data[j][i]}"
                current_total = eval(expression)
        overall_total += current_total
    return overall_total

def do_the_math_other(data):
    total_count = 0
    skip = False
    values = []
    current_str = ""
    for j in range(len(data[0])):
        for i in range(len(data)):
            if not skip:
                if data[i][j].isdigit():
                    current_str += data[i][j]
                elif data[i][j] != " ":
                    current_operator = data[i][j]
                    skip = True
        if current_str != "":
            values.append(current_str)
        current_str = ""
        if skip:
            total_count += evaluate(current_operator, values)
            skip = False
            values = []
            current_str = ""

                
    return total_count

def evaluate(current_operator, values):
    expression = reduce(lambda x, y: x + current_operator + y, values)
    #print(expression)
    return eval(expression)

def main():
    print("Part 1:")
    data = import_data()
    print(do_the_math(data))
    print("Part 2:")
    data_other = import_data_other()
    print(do_the_math_other(data_other))

main()


        