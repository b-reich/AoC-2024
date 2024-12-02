from typing import List


def is_safe_line(line: List[int]) -> bool:
    within_range = all(abs(line[i+1] - line[i]) <=
                       3 for i in range(len(line) - 1))

    is_increasing = all(line[i+1] > line[i] for i in range(len(line) - 1))
    is_decreasing = all(line[i+1] < line[i] for i in range(len(line) - 1))

    return within_range and (is_increasing or is_decreasing)


def can_be_safe_by_removing_one(line: List[int]) -> bool:
    for i in range(len(line)):
        # Create a new line without the i-th element
        new_line = line[:i] + line[i+1:]
        if is_safe_line(new_line):
            return True
    return False


def part1() -> int:
    with open("02/input", "r") as file:
        data = [list(map(int, line.split())) for line in file.readlines()]

    results = [is_safe_line(line) for line in data]
    return results.count(True)


def part2() -> int:
    with open("02/input", "r") as file:
        data = [list(map(int, line.split())) for line in file.readlines()]

    results = []
    for line in data:
        if is_safe_line(line):
            results.append(True)
        elif can_be_safe_by_removing_one(line):
            results.append(True)
        else:
            results.append(False)
    return results.count(True)


if __name__ == "__main__":
    print("Part1: " + str(part1()))
    print("Part2: " + str(part2()))
