# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def translate_vowel(text, replacement):
    translated = ""

    for letter in text:
        if is_vowel(letter):
            translated += replacement
        else:
            translated += letter

    return translated


def is_vowel(letter):
    return letter in "AÄEIOÖUüaäeioöuü"


def translate_vowel_shorter(text, replacement):
    vowels = "AÄEIOÖUüaäeioöuü"
    trans_dict = text.maketrans(vowels, replacement * len(vowels))
    return text.translate(trans_dict)





def main():
    print(translate_vowel("Reiseführer", "?"))
    print(translate_vowel("Rasenmäher", "-"))
    print(translate_vowel("Tischtennis", "_"))
    print(translate_vowel("Ratespiel", "_"))

    print(translate_vowel("Rasenmäher", ""))
    print(translate_vowel("Reiseführer", ""))

    print(translate_vowel("Der Reiseführer empfiehlt Java", "-"))
    print(translate_vowel("Fit durch die Python Challenge", "-"))

    print(translate_vowel_shorter("Der Reiseführer empfiehlt Java", "-"))
    print(translate_vowel_shorter("Fit durch die Python Challenge", "-"))


if __name__ == "__main__":
    main()
