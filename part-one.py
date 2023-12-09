#!/usr/bin/env python3

import os
from time import perf_counter_ns

class Node:
    nodes = {}

    def connect_all():
        for node in Node.nodes.values():
            node.connect()

    def __init__(self, data):
        self.name = data[0:3]
        self.leftName = data[7:10]
        self.rightName = data[12:15]
        self.left = None
        self.right = None
        Node.nodes[self.name] = self

    def connect(self):
        self.left = Node.nodes[self.leftName]
        self.right = Node.nodes[self.rightName]

    def move(self, dir):
        return self.left if dir == 'L' else self.right

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        data = input.read().split('\n')

    instructions = data[0]
    _ = [Node(line) for line in data[2:]]
    Node.connect_all()

    answer = 0
    instructions_length = len(instructions)
    current_node = Node.nodes['AAA']
    while current_node.name != 'ZZZ':
        current_node = current_node.move(instructions[answer % instructions_length])
        answer += 1

    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
