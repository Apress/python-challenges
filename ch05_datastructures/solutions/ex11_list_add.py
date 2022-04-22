# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def list_add(values1, values2):
    result = []

    carry = 0

    for i in range(len(values1) - 1, -1, -1):
        value1 = values1[i]
        value2 = values2[i]

        sum = value1 + value2 + carry
        result.insert(0, sum % 10)

        carry = 1 if sum >= 10 else 0

    #   add another element if last one has a carry
    if carry == 1:
        result.insert(0, 1)

    return result


def list_add_with_zip(values1, values2):
    result = []

    carry = 0

    # 'zip' object is not reversible
    for value1, value2 in reversed(list(zip(values1, values2))):
        sum = value1 + value2 + carry
        result.insert(0, sum % 10)

        carry = 1 if sum >= 10 else 0

    #   add another element if last one has a carry
    if carry == 1:
        result.insert(0, 1)

    return result



def list_add_with_iter(values1, values2):
    result = []
    carry = 0

    backiterator1 = reversed(values1)
    backiterator2 = reversed(values2)
    while True:
        try:
            value1 = next(backiterator1)
            value2 = next(backiterator2)

            sum = value1 + value2 + carry
            result.insert(0, sum % 10)

            carry = 1 if sum >= 10 else 0
        except StopIteration:
            break

    # Übertrag berücksichtigen
    if carry == 1:
        result.insert(0, 1)

    return result


def list_add_improved(values1, values2):
    result = []

    carry = 0

    idx1 = len(values1) - 1
    idx2 = len(values2) - 1

    while idx1 >= 0 or idx2 >= 0:
        value1 = safe_get_at(values1, idx1)
        value2 = safe_get_at(values2, idx2)

        sum = value1 + value2 + carry
        result.insert(0, sum % 10)

        carry = 1 if sum >= 10 else 0

        idx1 -= 1
        idx2 -= 1

    # Übertrag berücksichtigen
    if carry == 1:
        result.insert(0, 1)

    return result


def safe_get_at_old(inputs, pos):
    if 0 <= pos < len(inputs):
        return inputs[pos]

    return 0


def safe_get_at(inputs, pos):
    try:
        return inputs[pos]
    except IndexError:
        return 0


def list_add_inverse(inputs1, inputs2):
    result = []

    carry = 0

    idx = 0
    while idx < len(inputs1) or idx < len(inputs2):
        value1 = safe_get_at(inputs1, idx)
        value2 = safe_get_at(inputs2, idx)

        sum = value1 + value2 + carry
        carry = 1 if sum >= 10 else 0

        result.append(sum % 10)
        idx += 1

    # Übertrag berücksichtigen
    if carry == 1:
        result.append(1)

    return result


def main():
    print(list_add([1, 2, 3], [4, 3, 2]))
    print(list_add([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]))
    print(list_add([9, 9, 9], [9, 9, 9]))
    print(list_add([1, 2, 3], [1, 4, 3, 2]))


    print(list_add_with_zip([1, 2, 3], [4, 3, 2]))
    print(list_add_with_zip([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]))
    print(list_add_with_zip([9, 9, 9], [9, 9, 9]))
    print(list_add_with_zip([1, 2, 3], [1, 4, 3, 2]))


    print(list_add_improved([1, 2, 3, 4], [7, 7, 7, 6, 5, 4, 3]))

    print(list_add_inverse([1, 4, 3, 2, 1], [1, 3, 4, 5, 6, 7, 7, 7]))


if __name__ == "__main__":
    main()
