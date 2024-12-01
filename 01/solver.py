from typing import List


def main():
    with open("01/input", "r") as file:
        data = [tuple(map(int, line.split())) for line in file.readlines()]

    column1, column2 = zip(*data)

    # Sort each column
    sorted_column1 = sorted(column1)
    sorted_column2 = sorted(column2)

    sorted_list = list(zip(sorted_column1, sorted_column2))
    result = sum([abs(a - b) for a, b in sorted_list])
    print(result)


if __name__ == "__main__":
    print(main())
