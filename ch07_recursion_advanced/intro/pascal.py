# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import time


def pascal_rec(row, col):
    # rekursiver Abbruch: Spitze
    if col == 1 and row == 1:
        return 1

    # rekursiver Abbruch: Ränder
    if col == 1 or col == row:
        return 1

    # rekursiver Abstieg
    return pascal_rec(row - 1, col) + pascal_rec(row - 1, col - 1)


def pascal_optimized(row, col):
    return calc_pascal_memo(row, col, {})


def calc_pascal_memo(row, col, lookup_map):
    # MEMOIZATION
    key = (row, col)
    if key in lookup_map:
        return lookup_map[key]

    result = 0
    # rekursiver Abbruch: Spitze
    if col == 1 and row == 1:
        return 1

    # rekursiver Abbruch: Ränder
    if col == 1 or col == row:
        return 1
    else:
        # rekursiver Abstieg
        result = calc_pascal_memo(row - 1, col, lookup_map) + \
                 calc_pascal_memo(row - 1, col - 1, lookup_map)

    # MEMOIZATION
    lookup_map[key] = result

    return result


def main():
    start = time.process_time()
    print("pascalRec(30, 15)", pascal_rec(30, 15))
    end = time.process_time()
    print("pascalRec(30, 15) took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    print("pascalOptimized(30, 15)", pascal_optimized(30, 15))
    end = time.process_time()
    print("pascalOptimized(30, 15) took %.2f ms" % ((end - start) * 1000))

    # Dauert sehr lange => über 1 Stunde?
    #start = time.process_time()
    #print("pascalRec(42, 15)", pascalRec(42, 15))
    #end = time.process_time()
    #print("pascalRec(42, 15) took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    print("pascalOptimized(42, 15)", pascal_optimized(42, 15))
    end = time.process_time()
    print("pascalOptimized(42, 15) took %.2f ms" % ((end - start) * 1000))


if __name__ == "__main__":
    main()
