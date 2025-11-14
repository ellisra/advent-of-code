#include "../common/utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int part1(const char *input);
int part2(const char *input);

int main() {
    char *input = read_file("../inputs/2015/day01.txt");
    if (!input) return 1;

    printf("Part 1: %d\n", part1(input));
    printf("Part 2: %d", part2(input));

    free(input);
    return 0;
}

int part1(const char *input) {
    int count = 0;
    const char *tmp = input;
    while ((tmp = strstr(tmp, "("))) {
        count++;
        tmp++;
    }

    return 2 * count - strlen(input);
}

int part2(const char *input) {
    int floor = 0;
    for (int i = 0; i < strlen(input); i++) {
        if (floor < 0) return i;

        if (input[i] == '(') {
            floor++;
        } else {
            floor--;
        }
    }

    return 0;
}
