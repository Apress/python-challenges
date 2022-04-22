# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def capitalize(input):
    input_chars = list(input)

    capitalize_next_char = True
    for i, current_char in enumerate(input_chars):
        if current_char.isspace():
            capitalize_next_char = True
        elif capitalize_next_char and current_char.isalpha():
            input_chars[i] = current_char.upper()
            capitalize_next_char = False

    return "".join(input_chars)


def capitalize_shorter(input):
    converted = [word[0].upper() + word[1:] for word in input.split()]
    return " ".join(converted)


def capitalize_special(input):
    input_chars = list(input)

    capitalize_next_char = True
    for i, current_char in enumerate(input_chars):

        if current_char.isspace():
            capitalize_next_char = True
        elif capitalize_next_char:
            input_chars[i] = current_char.upper()
            capitalize_next_char = False

    return "".join(input_chars)


def capitalize_words(words):
    return [capitalize_word(word) for word in words]


def capitalize_words_old(words):
    capitalized_words = []

    for word in words:
        capitalized_words.append(capitalize_word(word))

    return capitalized_words


def capitalize_word(word):
    if not word:
        return ""

    return word[0].upper() + word[1:]


def capitalize_special_2(words, ignorable_words):
    capitalized_words = []

    for word in words:
        if word in ignorable_words:
            capitalized_words.append(word)
        else:
            capitalized_words.append(capitalize_word(word))

    return capitalized_words




def main():
    print(capitalize("alles scheint in ordnung"))
    print(capitalize("Dies ist ein text"))
    print(capitalize("Dies \t ist   ein   text"))
    print(capitalize("what a wonderful day and feature"))

    print(capitalize_shorter("alles scheint in ordnung"))
    print(capitalize_shorter("Dies ist ein text"))
    print(capitalize_shorter("Dies \t ist   ein   text"))

    print(capitalize_word("micha el"))
    print(capitalize_word(""))
    print("Dies ist ein text".title())
    print("what a wonderful day and feature".title())


if __name__ == "__main__":
    main()
