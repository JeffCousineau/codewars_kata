import codewars_test as Test

def snail(array):
    if array:
        if array[0]:
            print(array)
        else: return []
    else: return []
    cur_pos = (0,0)
    count = 0
    direction = 1 # 1=right, 2=down, 3=left, 4=up
    final_array = []
    size = len(array[0])
    visited_array = [[False for i in range(size)] for j in range(size)]
    end = False
    #print(visited_array[cur_pos[0]][cur_pos[1]])
    while not end:
        if visited_array[cur_pos[0]][cur_pos[1]] == False:
            final_array.append(array[cur_pos[0]][cur_pos[1]])
            visited_array[cur_pos[0]][cur_pos[1]] = True
            
        if direction == 1 and is_valid(visited_array,[cur_pos[0],cur_pos[1]+1]):
            cur_pos = [cur_pos[0],cur_pos[1]+1]
        elif direction == 2 and is_valid(visited_array,[cur_pos[0]+1,cur_pos[1]]):
            cur_pos = [cur_pos[0]+1,cur_pos[1]]
        elif direction == 3 and is_valid(visited_array,[cur_pos[0],cur_pos[1]-1]):
            cur_pos = [cur_pos[0],cur_pos[1]-1]
        elif direction == 4 and is_valid(visited_array,[cur_pos[0]-1,cur_pos[1]]):
            cur_pos = [cur_pos[0]-1,cur_pos[1]]
        else:
            count += 1
            direction = next_direction(direction)
        if count > 100:
            end = True
            
        #print(direction)
            
    return final_array
def next_direction(direction):
    if direction == 4:
        return 1
    else: return (direction + 1)
    
def is_valid(visited_array, pos):
    #print(len(visited_array[0]))
    #print(pos)
    if pos[0] >= len(visited_array[0]) or pos[1] >= len(visited_array[0]):
        return False
    else:
        if visited_array[pos[0]][pos[1]] == False:
            return True
        else: return False


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
Test.assert_equals(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
Test.assert_equals(snail(array), expected)