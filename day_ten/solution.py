from itertools import combinations_with_replacement, combinations
import time
from pulp import *
def import_data():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        data = []
        for line in lines:
            #[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
            button_string = line[line.find("(")+1: line.rfind(")")].split(") (")
            interim_buttons = list(map(lambda button_list: button_list.split(","), button_string))
            buttons = []
            for button_list in interim_buttons:
                buttons.append(list(map(int, button_list)))
            joltages = line[line.find("{")+1:line.find("}")].split(",")
            joltages = list(map(int, joltages))

            data.append({"config": list(line[line.find("[")+1:line.find("]")]), "buttons": buttons, "joltages": joltages})
        return data

def configure_machine(machine_spec):
    counter = 0
    desired_config = machine_spec["config"]
    current_config = []
    for i in range(len(desired_config)):
        current_config.append(".")
    while desired_config != current_config:
        counter += 1
        button_pushes = list(combinations(machine_spec["buttons"], counter))
        for button_push_combination in button_pushes:
            candidate_config = current_config
            for button in button_push_combination:
                candidate_config = apply_button(button,candidate_config)
            if candidate_config == desired_config:
                return counter

def calculate_total_machine_config_pushes(data):
    counter = 0 
    for machine_spec in data:
        counter += configure_machine(machine_spec)
    return counter

def apply_button(button, current_config):
    new_config = []
    for i, light in enumerate(current_config):
        if i in button:
            new_config.append(toggle(light))
        else:
            new_config.append(light)
    return new_config

def toggle(string):
    if string == "#":
        return "."
    return "#"

def apply_joltage_button(button, current_config):
    new_config = []
    for i, joltage in enumerate(current_config):
        if i in button:
            new_config.append(joltage + 1)
        else:
            new_config.append(joltage)
    return new_config

def configure_machine_joltage(machine_spec):
    counter = 0
    desired_config = machine_spec["joltages"]
    current_config = []
    for i in range(len(desired_config)):
        current_config.append(0)
    while desired_config != current_config:
        counter += 1
        print(f"\t{counter}")
        button_pushes = list(combinations_with_replacement(machine_spec["buttons"], counter))
        for button_push_combination in button_pushes:
            candidate_config = current_config
            for button in button_push_combination:
                candidate_config = apply_joltage_button(button,candidate_config)
            if candidate_config == desired_config:
                return counter

def total_steps_joltage_machine(machine):
    print("machine")
    current_config = machine["joltages"]
    buttons = machine["buttons"]
    queue = set()
    queue.add((tuple(current_config), 0))
    new_queue = set()
    while True:
        for step in queue:
            if len(list(filter(lambda x: x != 0, step[0]))) == 0:
                return step[1]
            elif len(list(filter(lambda x: x < 0, step[0]))) == 0:
                for button in buttons:
                    new_queue.add((tuple(reduce_by_joltage(step[0], button)), step[1]+1))
        print(f"\t{len(new_queue)}")
        queue = new_queue
        new_queue = set()

def reduce_by_joltage(current_joltage, button):
    new_config = []
    for i, joltage in enumerate(current_joltage):
        if i in button:
            new_config.append(joltage - 1)
        else:
            new_config.append(joltage)
    return new_config


def calculate_total_joltage_config_pushes(data):
    counter = 0 
    for machine_spec in data:
        counter += min_solve_machine(machine_spec)
    return counter

def min_solve_machine(machine):
    print(machine)
    count = 0
    prob = LpProblem("The_joltage_problem", LpMinimize)
    buttons = []
    for i, button in enumerate(machine["buttons"]):
        buttons.append(f"BUTTON_{i}")
        
    button_vectors = {}
    for j, button in enumerate(machine["buttons"]):
        vector = []
        for i in range(len(machine["joltages"])):
            if i in button:
                vector.append(1)
            else:
                vector.append(0)
        button_vectors[f"BUTTON_{j}"] = tuple(vector)
    for key in button_vectors.keys(): 
        print(f"{key}: {button_vectors[key]}") 

    button_vars = LpVariable.dicts("Butn", buttons, lowBound = 0, cat='Integer')

    prob += (
        lpSum(1*button_vars[i] for i in buttons),
        "Total button pushes",
    )

    for index in range(len(machine["joltages"])):
        prob += (
            lpSum([button_vectors[i][index] * button_vars[i] for i in buttons]) == machine["joltages"][index],
            f"Joltage value {index}: {machine["joltages"][index]}",
        )
    
    prob.writeLP("JoltageProblem.lp")

    prob.solve()

    #print("Status", LpStatus[prob.status])

    for v in prob.variables():
        print(v.name, "=", v.varValue)
        count+= v.varValue
    return count




def main():
    print("Part 1:")
    data = import_data()
    print(calculate_total_machine_config_pushes(data))
    print("Part 2:")
    print(calculate_total_joltage_config_pushes(data))

main()