#!/usr/bin/env python3

from collections import defaultdict


with open('../inputs/2015/day13.txt') as file:
    data = [line.rstrip('.').split(' ') for line in file.read().splitlines()]

people = defaultdict(dict)
for line in data:
    people[line[0]][line[-1]] = int(line[3]) if line[2] == 'gain' else -int(line[3])

print(people)
