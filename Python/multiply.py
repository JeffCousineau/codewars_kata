import codewars_test as test

def multiply(a, b):
  return a * b

test.describe("Testing multiply")
test.assert_equals(multiply(5,6), 30)
test.assert_equals(multiply(0,8), 0)