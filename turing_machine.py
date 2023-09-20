import json
import random


class TuringMachine:

    def __init__(self, rules:list):
        self.rules = rules


    def step(self, tape:list, num:int, state:int):
        current_bit = tape[num]
        current_rule = self.rules[state][current_bit]
        tape[num] = current_rule["new_bit"]
        num += current_rule["new_dir"]
        num = num % len(tape)
        state = current_rule["new_state"]
        return tape, num, state


    def calc(self, tape:list, num:int, state:int, steps:int, verbose=False):
        for r in range(steps):
            if verbose: print(tape)
            tape, num, state = self.step(tape, num, state)
        if verbose: print(tape)
        return tape


def machine_from_json(file: str):
    return TuringMachine(json.load(open(file)))


def _random_rule(size: int):
    return {
        "new_bit": random.choice([0, 1]),
        "new_dir": random.choice([-1, 1]),
        "new_state": random.randrange(size)
    }


def create_random_machine(size: int):
    rules = []
    for i in range(size):
        rules.append([
            _random_rule(size),
            _random_rule(size)
        ])
    return TuringMachine(rules)


def create_random_start(tape_size, state_num):
    tape = [0]*tape_size
    for i in range(tape_size):
        tape[i] = random.choice([0, 1])
    return tape, random.randrange(tape_size), random.randrange(state_num)

def create_zero_start(tape_size):
    tape = [0]*tape_size
    for i in range(tape_size):
        tape[i] = 0
    return tape, 0, 0
