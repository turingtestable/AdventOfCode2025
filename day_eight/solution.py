from collections import defaultdict
from functools import reduce
import math

distances = {}
circuits = defaultdict(list)

def import_data():
    with open("input.txt") as file:
        return file.read().splitlines()
        

def distance(point1, point2):
    p1 = list(map(int, point1.split(",")))
    p2 = list(map(int, point2.split(",")))

    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def shortest_connections(data, num_connections_needed):
    global defaultdict
    global distances
    counter = 0
    for index, coord in enumerate(data):
        distance_dict = {}
        for index_other, coord_other in enumerate(data):
            if index < index_other:
                distance_dict[distance(coord, coord_other)] = coord_other
        distances[coord] = dict(sorted(distance_dict.items()))

    while counter < num_connections_needed:
        current_min_distance = 10000000.0
        best_coord = ""
        for coord in distances.keys():
            if bool(distances[coord]):
                min_coord_distance = list(distances[coord].keys())[0]
                if min_coord_distance < current_min_distance:
                    best_coord = coord
                    current_min_distance = min_coord_distance
        circuits[best_coord].append(distances[best_coord][current_min_distance])
        circuits[distances[best_coord][current_min_distance]].append(best_coord)
        distances[best_coord].pop(current_min_distance)
        counter += 1
    return size_largest_circuits(circuits)

def size_largest_circuits(circuits):
    used = defaultdict(bool)
    max_circuit_sizes = [0,0,0]
    for circuit in circuits.keys():
        current_circuit_size = 0
        if not used[circuit]:
            used[circuit] = True
            neighbors = circuits[circuit]
            current_circuit_size = 1
            while neighbors != []:
                neighbor = neighbors.pop()
                if not used[neighbor]:
                    current_circuit_size += 1
                    neighbors += circuits[neighbor]
                    used[neighbor] = True
        max_circuit_sizes.append(current_circuit_size)
        max_circuit_sizes = sorted(max_circuit_sizes)[1:]
    return reduce(lambda x,y: x*y, max_circuit_sizes)


def is_already_connected(p1, p2, circuits):
    current = p1
    neighbors = [] + circuits[current]
    visited = []
    while circuits[current] != [] and neighbors != []:
        if not current in visited:
            visited.append(current)
            if p2 in circuits[current]:
                return True
            neighbors += circuits[current]
        current = neighbors.pop()
    return False

def not_connected(data, circuits):
    if len(circuits.keys()) < len(data):
        return True
    else:
        return False
        

def distance_final_connection(data):
    current_x_distance = 0
    while not_connected(data,circuits):
        current_min_distance = 10000000000.0
        best_coord = ""
        for coord in distances.keys():
            if bool(distances[coord]):
                min_coord_distance = list(distances[coord].keys())[0]
                if min_coord_distance < current_min_distance:
                    best_coord = coord
                    current_min_distance = min_coord_distance
        current_x_distance = int(best_coord.split(",")[0]) * int(distances[best_coord][current_min_distance].split(",")[0])
        circuits[best_coord].append(distances[best_coord][current_min_distance])
        circuits[distances[best_coord][current_min_distance]].append(best_coord)
        distances[best_coord].pop(current_min_distance)
    return current_x_distance

def size_largest_circuit(circuits):
    used = defaultdict(bool)
    max_circuit_size = 0
    for circuit in circuits.keys():
        current_circuit_size = 0
        if not used[circuit]:
            used[circuit] = True
            neighbors = circuits[circuit]
            current_circuit_size = 1
            while neighbors != []:
                neighbor = neighbors.pop()
                if not used[neighbor]:
                    current_circuit_size += 1
                    neighbors += circuits[neighbor]
                    used[neighbor] = True
        max_circuit_size = max(max_circuit_size, current_circuit_size)
    return max_circuit_size



def main():
    print("Part 1")
    data = import_data()
    print(shortest_connections(data, 1000))
    print("Part 2")
    print(distance_final_connection(data))

main()
