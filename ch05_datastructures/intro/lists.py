# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def remove_all_inplace(values, item):
    try:
        while True:
            values.remove(item)
    except ValueError:
        pass


def remove_all_inplace_improved(list, value):
    while value in list:
        list.remove(value)


def remove_all_v2(values, item):
    return [value for value in values if value != item]


def remove_all_v3(values, item):
    filter_ = filter(lambda x: x != item, values)
    print(filter_)
    return list(filter_)


def remove_all_fast(values, item):
    write_idx = 0
    for i, value in enumerate(values):
        if value != item:
            values[write_idx] = value
            write_idx += 1

    return values[:write_idx]


def collect_all(values, condition):
    result = []
    for elem in values:
        if condition(elem):
            result.append(elem)
    return result


def collect_all_v2(values, condition):
    return [elem for elem in values if condition(elem)]


def collect_all_v3(values, condition):
    return list(filter(condition, values))


def main():
    names = ["Tim", "Tom", "Mike", "Mike", "Mike"]
    remove_all_inplace(names, "Mike")
    print(names)

    names = ["Tim", "Tom", "Mike", "Mike", "Mike"]
    remove_all_inplace_improved(names, "Mike")
    print(names)

    names = remove_all_v2(["Tim", "Tom", "Mike", "Mike", "Mike"], "Mike")
    print(names)

    names3 = ["Tim", "Tom", "Mike", "Mike", "Mike"]
    names3 = remove_all_v3(names3, "Mike")
    print(names3)

    names = remove_all_fast(["Tim", "Tom", "Mike", "Mike", "Mike"], "Mike")
    print(names)

    names = ["Tim", "Tom", "Mike", "Mike", "Mike"]
    print(collect_all(names, lambda value: value == "Mike"))

    names2 = ["Tim", "Tom", "Mike", "Mike", "Mike"]
    names2 = collect_all_v2(names2, lambda value: value == "Mike")
    print(names2)

    names3 = ["Tim", "Tom", "Mike", "Mike", "Mike"]
    names3 = collect_all_v3(names3, lambda value: value == "Mike")
    print(names3)


if __name__ == "__main__":
    main()
