import codewars_test as test

def spin_words(sentence):
    words = sentence.split(" ")
    final_string = ""
    for i in words:
        if len(i) >= 5: final_string+=(i[::-1])
        else: final_string += i
        final_string += " "
    return final_string[:-1]

test.assert_equals(spin_words("Welcome"), "emocleW")
