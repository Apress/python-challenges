# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def calc_armstrong_numbers():
    results = []

    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                numeric_value = x * 100 + y * 10 + z
                cubic_value = int(pow(x, 3) + pow(y, 3) + pow(z, 3))

                if numeric_value == cubic_value:
                    results.append(numeric_value)

    return results


def calc_numbers(cubic_function):
    results = []
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                numeric_value = x * 100 + y * 10 + z
                cubic_value = int(cubic_function(x, y, z))
                if numeric_value == cubic_value:
                    results.append(numeric_value)
    return results


def main():
    print(calc_armstrong_numbers())

    def special1(x, y, z):
        return int(pow(x, 3) + pow(y, 3) + pow(z, 3))

    def special2(x, y, z):
        return int(pow(x, 1) + pow(y, 2) + pow(z, 3))

    def special3(x, y, z):
        return int(pow(x, 3) + pow(y, 2) + pow(z, 1))

    print(calc_numbers(special1))
    print(calc_numbers(special2))
    print(calc_numbers(special3))

    print(calc_numbers(lambda x, y, z: int(pow(x, 3) + pow(y, 3) + pow(z, 3))))
    print(calc_numbers(lambda x, y, z: int(pow(x, 3) + pow(y, 3) + pow(z, 3))))


if __name__ == "__main__":
    main()
