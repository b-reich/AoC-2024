import re
import mmap
from typing import List
from collections import defaultdict, deque


def check(update: List[int], rules: List[tuple]) -> bool:
    for page_a, page_b in rules:
        if page_a in update and page_b in update:
            if update.index(page_a) > update.index(page_b):
                return False
    return True


def get_middle_value(update: List[int]) -> int:
    mid_index = len(update) // 2
    return update[mid_index]


def reorder_update(update: List[int], rules: List[tuple]) -> List[int]:
    dependencies = defaultdict(set)
    for page_a, page_b in rules:
        if page_a in update and page_b in update:
            dependencies[page_b].add(page_a)

    ordered = []
    no_dependencies = deque(
        [page for page in update if not dependencies[page]])

    while no_dependencies:
        current = no_dependencies.popleft()
        ordered.append(current)

        for page in list(dependencies):
            dependencies[page].discard(current)
            if not dependencies[page]:
                no_dependencies.append(page)
                del dependencies[page]

    return ordered


def part1() -> int:
    with open("05/input", "r") as file:
        data = file.read()

    rules_raw, updates_raw = data.strip().split("\n\n")

    rules = [tuple(map(int, line.split('|')))
             for line in rules_raw.strip().split('\n')]

    updates = [list(map(int, line.split(',')))
               for line in updates_raw.strip().split('\n')]
    valid_updates = [update for update in updates if check(update, rules)]

    medians = [get_middle_value(update) for update in valid_updates]
    total_median_sum = sum(medians)

    return total_median_sum


def part2() -> int:
    with open("05/input", "r") as file:
        data = file.read()

    rules_raw, updates_raw = data.strip().split("\n\n")

    rules = [tuple(map(int, line.split('|')))
             for line in rules_raw.strip().split('\n')]
    updates = [list(map(int, line.split(',')))
               for line in updates_raw.strip().split('\n')]

    invalid_updates = [
        update for update in updates if not check(update, rules)]

    reordered_updates = [reorder_update(update, rules)
                         for update in invalid_updates]

    medians = [get_middle_value(update) for update in reordered_updates]
    total_median_sum = sum(medians)

    return total_median_sum


if __name__ == "__main__":
    print("Part1: " + str(part1()))
    print("Part2: " + str(part2()))
