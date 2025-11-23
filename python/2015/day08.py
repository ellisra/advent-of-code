import ast
import json


if __name__ == '__main__':
    lines = [line.rstrip() for line in open('../inputs/2015/day08.txt')]

    print(f"Part 1: {sum([len(l) - len(ast.literal_eval(l)) for l in lines])}")
    print(f"Part 2: {sum([len(json.dumps(l)) - len(l) for l in lines])}")
