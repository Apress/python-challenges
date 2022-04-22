# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def generate_following_values(current_value, sequence_length):
    result = []

    while sequence_length > 0:
        result.append(current_value)
        current_value += 1
        sequence_length -= 1

    return result



def generate_following_values_v2(current_value, sequence_length):
    return [value for value in range(current_value,
                                     current_value + sequence_length)]


def generate_following_values_built_in(current_value, sequence_length):
    return list(itertools.islice(itertools.count(current_value), sequence_length))


def generate_following_values_for_predefined(predefined_values,
                                             current_value,
                                             sequence_length):
    result = []

    current_pos = predefined_values.index(current_value)
    while sequence_length > 0:
        result.append(current_value)
        current_value, current_pos = next_cyclic(predefined_values,
                                                 current_pos)
        sequence_length -= 1

    return result


def next_cyclic(values, current_pos):
    next_pos = (current_pos + 1) % len(values)

    return values[next_pos], next_pos


def main():
    print(generate_following_values(1, 7))
    print(generate_following_values_v2(1, 7))

    print(generate_following_values_built_in(1, 7))
    print(generate_following_values_built_in(3, 11))

    ### Für eigene Arrays / "Enum"
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(generate_following_values_for_predefined(days, "Friday", 7))


if __name__ == "__main__":
    main()

