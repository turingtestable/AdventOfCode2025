tree_specs = []
presents = []
def import_data():
    with open("input.txt") as file:
        global tree_specs
        global presents
        lines = file.read().splitlines()
        reading_present = False
        current_present_total = 0
        for line in lines:
            if line.strip() == "":
                reading_present = False
                presents.append(current_present_total)
                current_present_total = 0
            elif line[1] == ":":
                reading_present = True
            elif "x" in line:
                line_list = line.split(": ")
                area = list(map(int, line_list[0].split("x")))
                presents_list = list(map(int, line_list[1].split(" ")))
                tree_specs.append([area, presents_list])
            elif reading_present:
                current_present_total += line.count("#")



def naive_packing():
    global tree_specs
    global presents
    count = 0
    for tree in tree_specs:
        area = tree[0][0]*tree[0][1]
        present_area = 0
        for i in range(len(tree[1])):
            present_area += tree[1][i]*presents[i]
        if present_area <= area:
            count+=1
    return count


def main():
    import_data()
    print(tree_specs)
    print(presents)
    print("Part 1:", naive_packing())


main()


