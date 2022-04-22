# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def collect_into_buckets(values, buckets):
    for current in values:
        buckets[current] += 1


def fill_result_from_buckets(buckets, results):
    result_pos = 0

    for i, count in enumerate(buckets):
        while count > 0:
            results[result_pos] = i

            count -= 1
            result_pos += 1


def bucket_sort(values, expected_max):
    buckets = [0] * (expected_max + 1)

    collect_into_buckets(values, buckets)

    results = [0] * len(values)

    fill_result_from_buckets(buckets, results)

    return results


def main():
    ages = [10, 50, 22, 7, 42, 111, 50, 7]
    expected_max = 150

    sorted_result = bucket_sort(ages, expected_max)
    expected_result = [7, 7, 10, 22, 42, 50, 50, 111]

    print("sorted_result: ", sorted_result)
    print("expected_result: ", expected_result)


if __name__ == "__main__":
    main()
