from collections import defaultdict
graph = {}
reverse_graph = defaultdict(set)
paths = {}

def import_data():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        global graph
        for line in lines:
            line_list = line.split(": ")
            graph[line_list[0]] = set(line_list[1].split(" "))
        # global reverse_graph
        # for key in graph.keys():
        #     for value in graph[key]:
        #         reverse_graph[value].add(key)
        # changes = True
        # while changes:
        #     print(graph)
        #     print(dict(reverse_graph))
        #     old_reverse_graph = len(reverse_graph["out"])
        #     print(old_reverse_graph)
        #     to_be_added = set()
        #     for value in reverse_graph["out"]:
        #         if graph[value] == {"out"}:
        #             for next_node in reverse_graph[value]:
        #                 print("\t", graph[next_node])
        #                 graph[next_node].add("out")
        #                 if value in graph[next_node]:
        #                     graph[next_node].remove(value)
        #                 to_be_added.add(next_node)
        #     for node in to_be_added:
        #         reverse_graph["out"].add(node)

                        
        #     changes = old_reverse_graph != len(reverse_graph["out"])
        # print(graph)
        # print(dict(reverse_graph))

def count_paths_with_dac_and_fft():
    total = 0
    a1 = traverse("svr", "fft", {})
    a2 = traverse("fft", "dac", {})
    a3 = traverse("dac", "out", {})
    b1 = traverse("svr", "dac", {})
    b2 = traverse("dac", "fft", {})
    b3 = traverse("fft", "out", {})
    return a1*a2*a3 + b1*b2*b3

def traverse(current, end, paths):
    total = 0
    if current == end:
        return 1
    if current == "out":
        return 0
    if current in paths:
        return paths[current]
    else:
        for next_node in graph[current]:
            total += traverse(next_node, end, paths)
        paths[current] = total
        return total

def main():
    import_data()
    print("done_importing")
    print("Part 1:", traverse("you", "out", {}))
    print("Part 2:", count_paths_with_dac_and_fft())

main()