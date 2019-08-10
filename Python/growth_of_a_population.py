import codewars_test as Test

def nb_year(p0, percent, aug, p):
    current_pop = p0
    year_count = 0
    while(current_pop < p):
        year_count += 1
        current_pop *= (1+percent/100)
        current_pop += aug
    return year_count

Test.describe("nb_year")
Test.it("Basic tests")
Test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
Test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
Test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)