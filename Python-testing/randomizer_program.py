# random practicing
import random
print(random.randint(1, 10))
print(random.random())
eggs = ['blue_egg', 'red_egg', 'white_egg']
print(random.choice(eggs))


# random guessing game
highest_number = 100
lowest_number = 1
random_number = random.randint(lowest_number, highest_number)
is_running = True
guesses = 0

print('-----------------------------------')
print('Number guessing game')
while is_running:
    user_guess = input('guess number of 1-100: ')
    if user_guess == '':
        user_guess = input('guess number of 1-100: ')
    else:
        user_number = int(user_guess)
        if user_number > highest_number or user_number < lowest_number:
            user_guess = input('guess number of 1-100: ')
            user_number = int(user_guess)
        elif user_number > random_number:
            print('too high. try again')
            guesses += 1
            print(f'trys {guesses}')
        elif user_number < random_number:
            print('too low. try again')
            guesses += 1
            print(f'trys {guesses}')
        elif user_number == random_number:
            print('Correct! you guessed the number')
            print(f'PC number: {random_number}. your number: {user_number}')
            print(f'you win {guesses} trys')
            break