# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


mapping = {"Micha": 49, "Peter": 42, "Tom": 27}
mapping["NEW"] = 42
mapping.update({"Jim": 37, "John": 55})
print(mapping)
print(mapping.items())
print(mapping.keys())
print(mapping.values())

# "contains key"
print("contains key Micha?", "Micha" in mapping)
print("Micha values:", mapping.pop("Micha"))
print("contains key Micha?", "Micha" in mapping.keys())

# "contains value"
print("contains value 55?", 55 in mapping.values())


def filter_dict(input_dict, key_value_condition):
    filtered_dict = dict()
    for key, value in input_dict.items():
        if key_value_condition((key, value)):
            filtered_dict[key] = value
    return filtered_dict


def filter_by_value(input_dict, value_condition):
    filtered_result = filter_dict(input_dict,
                                  lambda item: value_condition(item[1]))
    return filtered_result


cities_sizes = {"Köln": 1_000_000, "Kiel": 250_000, "Bremen": 550_000,
                "Zürich": 400_000, "Oldenburg": 170_000}

print(filter_dict(cities_sizes, lambda item: 200_000 <= item[1] <= 700_000))
filtered_cities = filter_by_value(cities_sizes,
                                  lambda size: 200_000 <= size <= 700_000)
print(filtered_cities)
print(set(filtered_cities.keys()))
