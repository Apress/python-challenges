# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def reverse(text):
    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        current_char = text[i]
        reversed_text += current_char

    return reversed_text


def reverse_nicer(text):
    reversed_text = ""

    for current_char in reversed(text):
        reversed_text += current_char

    return reversed_text


def reverse_inplace(text):
    original_chars = list(text)

    left = 0
    right = len(original_chars) - 1

    while left < right:
        left_char = original_chars[left]
        right_char = original_chars[right]

        original_chars[left] = right_char
        original_chars[right] = left_char
        left += 1
        right -= 1

    # Trick: Liste in String wandeln
    return "".join(original_chars)


def main():
    print(reverse("RACEcar"))
    print(reverse_nicer("RACEcar"))
    print(reverse_inplace("RACEcar"))


if __name__ == "__main__":
    main()
