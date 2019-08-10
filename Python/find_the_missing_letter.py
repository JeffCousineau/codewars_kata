import codewars_test as test

def find_missing_letter(chars):
    last = ""
    for i in chars:
        if last != "":
            if ord(i)-ord(last) > 1:
                return str(chr(ord(i)-1))
            else:
                last = i
        else:
            last = i

test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
