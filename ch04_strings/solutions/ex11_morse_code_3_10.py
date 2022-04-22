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


def convert_to_morse_code_V1(current_char):
    match current_char:
        case "E": return "."
        case "O": return "- - -"
        case "S": return ". . ."
        case "T": return "-"
        case "W": return ". - -"
        case _: return "?"

def convert_to_morse_code(current_char):
    value = "?"
    match current_char:
        case "E": value = "."
        case "O": value = "- - -"
        case "S": value = ". . ."
        case "T": value = "-"
        case "W": value = ". - -"

    return value

def main():
    print(to_morse_code("TWEET"))


if __name__ == "__main__":
    main()
