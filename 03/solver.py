import re
import mmap


def part1() -> int:
    with open("03/input", "r+") as file:
        data = file.read().rstrip()

    # pattern = r"mul\(\d+,\d+\)"
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)

    results = [int(a) * int(b) for a, b in matches]
    return sum(results)


def part2() -> int:
    with open("03/input", "r+") as file:
        data = file.read().rstrip()

    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"don't\(\)|do\(\)"

    all_matches = re.finditer(rf"{mul_pattern}|{control_pattern}", data)

    enabled = True
    results = []
    for match in all_matches:
        if match.group(0) == "don't()":
            enabled = False
        elif match.group(0) == "do()":
            enabled = True
        # It's a mul() and enabled
        elif enabled and match.group(1) and match.group(2):
            x, y = int(match.group(1)), int(match.group(2))
            results.append(x * y)

    return sum(results)


if __name__ == "__main__":
    print("Part1: " + str(part1()))
    print("Part2: " + str(part2()))
