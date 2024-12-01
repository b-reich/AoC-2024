from typing import List


def part1():
    with open("01/input", "r") as file:
        data = [tuple(map(int, line.split())) for line in file.readlines()]

    column1, column2 = zip(*data)

    # Sort each column
    sorted_column1 = sorted(column1)
    sorted_column2 = sorted(column2)

    sorted_list = list(zip(sorted_column1, sorted_column2))
    result = sum([abs(a - b) for a, b in sorted_list])
    return result


def part2():
    with open("01/input", "r") as file:
        data = [tuple(map(int, line.split())) for line in file.readlines()]

    column1, column2 = zip(*data)

    result = 0

    for num in column1:
        count_in_column2 = column2.count(num)  # Count occurrences in column2
        result += num * count_in_column2

    return result


if __name__ == "__main__":
    print("Part1: " + str(part1()))
    print("Part2: " + str(part2()))
