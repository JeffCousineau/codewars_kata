import codewars_test as test
from time import strptime

def driver(data):
  surname = data[2][0:5]
  while len(surname) < 5:
      surname += "9"
  decade = data[3][-2:-1]
  birth_month = data[3][3:6]
  month_nb = strptime(birth_month, '%b').tm_mon
  month_nb = month_nb + 50 if data[4] == "F" else month_nb
  month_nb = "0"+str(month_nb) if month_nb < 10 else str(month_nb)
  birth_day = data[3][:2]
  birth_year = data[3][-1:]
  initials = str(data[0][:1]) + str(data[1][:1])
  initials = initials + "9" if len(initials) < 2 else initials
  return surname.upper()+decade+month_nb+birth_day+birth_year+initials+"9AA"


test.describe("Example tests")

data = ["John", "James", "Smith", "01-Jan-2000", "M"]
test.it("Should return SMITH001010JJ9AA")
test.assert_equals(driver(data), "SMITH001010JJ9AA")

data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
test.it("Should return GIBBS862131J99AA")
test.assert_equals(driver(data), "GIBBS862131J99AA")

data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
test.it("Should return LEE99809021AR9AA")
test.assert_equals(driver(data), "LEE99809021AR9AA")
