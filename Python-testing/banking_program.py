# bank system

def show_balance(x):
    return f'${x:.2f}'
def deposit(x):
    return x
def withdraw(x, y):
    if x > y:
        return f'${x} is not your bank account'
    else:
        return x


def main():
    balance = 0
    is_running = True
    while is_running:
        print('********************')
        print('1.show balance')
        print('2.deposit')
        print('3.withdraw')
        print('4.exit')
        print('********************')
        choice = input('Choose (1-4): ')
        if choice == '1':
            print('::::::::::')
            print(show_balance(balance))
            print('::::::::::')
        elif choice == '2':
            print('____________________')
            amount_plus = float(input('Enter value: $'))
            print('____________________')
            balance += deposit(amount_plus)
        elif choice == '3':
            print('____________________')
            amount_minus = float(input('Enter value: $'))
            print('____________________')
            balance -= withdraw(amount_minus, balance)
        elif choice == '4':
            is_running = False
        else:
            print('Please Choose (1-4)')
    print('you exited')


# start
main()