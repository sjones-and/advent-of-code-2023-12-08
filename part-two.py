#!/usr/bin/env python3

import os
from time import perf_counter_ns
from math import lcm

class Node:
    nodes = {}

    def connect_all():
        for node in Node.nodes.values():
            node.connect()

    def reset_all():
        for node in Node.nodes.values():
            node.reset()

    def __init__(self, data):
        self.name = data[0:3]
        self.leftName = data[7:10]
        self.rightName = data[12:15]
        self.left = None
        self.right = None
        self.positions = {}
        self.period = None
        Node.nodes[self.name] = self

    def connect(self):
        self.left = Node.nodes[self.leftName]
        self.right = Node.nodes[self.rightName]

    def move(self, position, length, dir):
        output = self.left if dir == 'L' else self.right
        if position % length in self.positions.keys():
            self.period = position - self.positions[position % length]
            return self
        if self.name[-1] == 'Z':
            self.positions[position % length] = position
        return output
    
    def reset(self):
        self.positions = {}
        self.period = None

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        data = input.read().split('\n')

    instructions = data[0]
    _ = [Node(line) for line in data[2:]]
    Node.connect_all()

    instructions_length = len(instructions)
    positions = []
    for node in Node.nodes.values():
        if node.name[-1] == 'A':
            Node.reset_all()
            ix = 0
            current_node = node
            while not current_node.period:
                instruction = instructions[ix % instructions_length]
                current_node = current_node.move(ix, instructions_length, instruction)
                ix += 1
            positions.append(current_node.period)

    answer = lcm(*positions)
    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
