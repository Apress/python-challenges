# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch09_search_and_sort.solutions.ex02_partition import partition2, partition3


def test_partition2():
    assert partition2(list("ABAABBBAAABBBA")) == "AAAAAAABBBBBBB"


def test_partition3():
    assert partition3(list("ABACCBBCAACCBBA")) == "AAAAABBBBBCCCCC"
