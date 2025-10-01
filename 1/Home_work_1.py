# task1
import sys

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))

def calculation(a, b, c):
    return b * (a - c)

print(calculation(a,b,c))


#task2
order = input('Please make your order, we have shaurma, samsa, pirozhki:\n')
if order == 'shaurma':
    filling = input('For shaurma we have meat or chicken\n')
    if filling not in('meat', 'chicken'):
        print('Sorry,we do not have that filling')
        sys.exit()

elif order == 'samsa':
    filling = input('For samsa we have meat,cheese or chicken\n')
    if filling not in('meat','chicken','cheese\n'):
        print('Sorry,we do not have that filling')
        sys.exit()
    if filling == "cheese":
        answer = input('Sorry,we ran out of it . Would you like to wait for 15 minutes? Yes/no\n')
        if answer.lower() == "no" :
            sys.exit()

elif order == 'pirozhki':
    filling = input('For pirozhki we have potato or cabbage\n')
    if filling not in('potato','cabbage'):
        print('Sorry,we do not have that filling')
else:
    print('Sorry,we do not have that dish')
    sys.exit()

quantity = input('How many you want?\n')
warm = input('Would you like it to be warmed up?\n')
drink = input('What drink would you like - tea,coffe,cola or water?\n')
if not drink:
    drink = 'No drink'

print(f'Your order is {order}  ,   {quantity} pieces , with {filling} warmed: {warm} and  for a drink you ordered : {drink}')
