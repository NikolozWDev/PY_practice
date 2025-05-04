import random
def slots():
    slot = ['🎰', '🍒', '🎲', '💎']
    return slot

def slot_random():
    random_list = []
    i = 0
    while i < 3:
        random_list.append(random.choice(slots()))
        i += 1
    return random_list

def slot_row(bal):
    slot = slot_random()
    if slot[0] == slot[1] == slot[2]:
        if slot[0] == '🎰':
            bal = bal * 3
        elif slot[0] == '🍒':
            bal = bal * 4
        elif slot[0] == '🎲':
            bal = bal * 5
        elif slot[0] == '💎':
            bal = bal * 10
        print('you win')
    else:
        print('you loose')
    return bal



def main():
    print('--------------------------------')
    print('Welcome to slot machine')
    print('Symbols: 3x🎰   4x🍒   5x🎲   10x💎')
    print('--------------------------------')
    balance = 100
    is_running = True
    while is_running:
        bet = input('bet: $')
        if not bet.isdigit():
            continue
        elif int(bet) > balance or int(bet) <= 0:
            print('your bet is incorrect')
            continue
        bet = int(bet)
        balance -= bet
        print(balance)
        print('& & & & & & & & & & & &')
        print(' | '.join(slot_random()))
        print('& & & & & & & & & & & &')
        slot_row(balance)

# start
main()