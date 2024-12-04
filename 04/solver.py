import re
import mmap
from typing import List


def count_xmas(grid: List[str]) -> int:

    n, m = len(grid), len(grid[0])
    xmas = "XMAS"
    xmas_length = len(xmas)
    count = 0

    def check_direction(x, y, dx, dy):
        for i in range(xmas_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[nx][ny] != xmas[i]:
                return False
        return True

    for i in range(n):
        for j in range(m):
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if check_direction(i, j, dx, dy):
                    count += 1
    return count


def count_x_mas(grid: List[str]) -> int:
    n, m = len(grid), len(grid[0])
    mas = "MAS"
    mas_length = len(mas)
    count = 0

    def check_direction(x, y, dx, dy):
        for i in range(mas_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[nx][ny] != mas[i]:
                return False
        return True

    for i in range(1, n - 1):
        for j in range(1, m - 1):
           if (
               (check_direction(i - 1, j - 1, 1, 1) or check_direction(i + 1, j + 1, -1, -1)) and
               (check_direction(i - 1, j + 1, 1, -1) or check_direction(i + 1, j - 1, -1, 1))
           ):
               count += 1

    return count


def part1() -> int:
    with open("04/input", "r") as file:
        data = [line for line in file.readlines()]

    return count_xmas(data)


def part2() -> int:
    with open("04/input", "r") as file:
        data = [line for line in file.readlines()]

    return count_x_mas(data)


if __name__ == "__main__":
    print("Part1: " + str(part1()))
    print("Part2: " + str(part2()))
