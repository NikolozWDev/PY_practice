# for loops
for x in reversed(range(1, 11, 3)):
    print(x)
print('done')


phone_number = '525-324-423'
for x in phone_number:
    if x == '-':
        continue
    print(x)



# cart task
food = []
price = 0

while True:
    foods = input('(to leave write q / Q) Enter food: ')
    if foods.lower() == 'q':
        break
    elif foods == '':
            foods = input('(to leave write q / Q) Enter food: ')
            continue
    else:
        food.append(foods)
        prices = input('Enter price: $')
        if prices == '':
            prices = input('Enter price: $')
            continue
        else:
            price += float(prices)

print('-----YOUT CART-----')
i = 0
while i < len(food):
    print(f'{food}')
    i += 1
print(f'your total price is: ${price}')




# lists []; sets {}; tuples ();
list = ['apple', 'banana', 'orange']
i = 0
while i < len(list):
    print(list[i])
    i += 1
list.append('kiwi')
print(list.index('banana'))


# rectangle
rows = int(input('Enter number of rows: '))
columns = int(input('Enter number of columns: '))
symbol = input('Enter symbol: ')

i = 0
while i < rows:
    print(symbol * columns)
    i += 1



# timer
import time

# time.sleep(3)
# print('done')
timer = int(input('Enter time in seconds: '))
i = timer
while i <= timer:
    seconds = i % 60
    minutes = int((i / 60)) % 60
    hours = int((i / 3600))
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

    if(i == 1):
        break
    i -= 1
print('times up')