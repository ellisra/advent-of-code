#!/usr/bin/env python3

from hashlib import md5

from common.constants import INPUT_DIR

with open(INPUT_DIR + '2015/day04.txt') as file:
    key = file.read().strip()

num = 0
while True:
    if md5((key + str(num)).encode()).hexdigest().startswith('000000'):
        print(num)
        break
    num += 1
