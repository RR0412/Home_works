import math
#task 1
# yoda = ['on Python', 'programming', 'I like ' ]
#
# print(f'{yoda[2]} {yoda[1]} {yoda[0]}')

#task 2

# marks = {'Bill': int(input('Enter mark for Bill:\n')),
#          'Jane': int(input('Enter mark for Jane:\n')),
#          'John': int(input('Enter mark for John:\n')),
#          'Mary': int(input('Enter mark for Mary:\n')),
#          }
# total = 0
# for value in marks.values():
#     total += value
#
# average = math.ceil(total/len(marks))
# print(f'Average mark:{average}')

#task 3

# for i in range(1,10):
#     print(f'5 * {i} = {i*5}')



array = []
total = 0
print('Enter numbers:\n')
while True:
    number = input()
    if number == 'end' :
        break
    array.append(int(number))
print(f'You entered:{array}')
for element in array:
    total += element
print(f'You entered:{array}')
print(f'Total: {math.ceil(total)}')
print(f'Average: {math.ceil(total/len(array))}')









