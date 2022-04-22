# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def to_morse_code(input):
    converted_msg = ""

    for current_char in input.upper():
        converted_letter = convert_to_morse_code(current_char)

        converted_msg += converted_letter
        converted_msg += "   "

    return converted_msg.strip()


def convert_to_morse_code(current_char):
    chars_to_morse = {"E": ".",
                      "O": "- - -",
                      "S": ". . .",
                      "T": "-",
                      "W": ". - -"}

    return chars_to_morse[current_char]


def main():
    print(to_morse_code("TWEET"))


if __name__ == "__main__":
    main()
