import codewars_test as test

def score(dice):
    final_score = 0
    current_dice = dice[:]
    # Test three 1's -> 1000 pts
    results = three_test(1,current_dice)
    final_score += results[1]
    for i in range(6,1,-1):
        results = three_test(i,results[0])
        final_score += results[1]
    if results[0]:
        final_score += results[0].count(1)*100
        final_score += results[0].count(5)*50
    return final_score
    
def three_test(number_to_test, dice):
    if dice:
        if(dice.count(number_to_test)>= 3):
            for i in range(0,3):
                del dice[dice.index(number_to_test)]
            return [dice,number_to_test*100 if number_to_test > 1 else number_to_test*1000]
    return [dice,0]

test.describe("Example Tests")
test.it("Example Case")
test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)