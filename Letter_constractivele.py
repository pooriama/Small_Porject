import collections


def is_letter_constractive(letter_text, magazine_text):

    letter_char= collections.Counter(letter_text)

    for c in magazine_text:
        if c in letter_char:
            letter_char[c]-=1
            if letter_char[c] == 0:
                del letter_char[c]
            if not letter_char:
                return True

    return not letter_char


print(is_letter_constractive("abcdef", "abcdefg"))



#second way

def is_letter_constrcutive_v2(letter_text, magazine_text):
    return not (collections.Counter(letter_text)-collections.Counter(magazine_text))


print(is_letter_constrcutive_v2("abcdefg", "abcdefg"))