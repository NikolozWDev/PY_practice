import random
import time

def main():
    slot_icons = ['🎰', '🍒', '🎲', '💎']
    balance = 100
    is_running = True
    print('************************************')
    print('Welcome Slot Machine')
    print('symbols: 2x🎰  3x🍒  4x🎲   0x💎')
    print('************************************')
    while is_running:
        slot_random = []
        i = 0
        while i < 3:
            slot_random.append(random.choice(slot_icons))
            i += 1
        bet = input('place your bet amount: $')
        if not bet.isdigit() or int(bet) > balance or int(bet) <= 0 or bet == '':
            print('Invalid')
            continue
        print('spinning...')
        time.sleep(1)
        bet = int(bet)
        balance -= bet
        print(' | '.join(slot_random))
        if slot_random[0] == slot_random[1] == slot_random[2]:
            print('you win')
            if slot_random[0] == '🎰':
                balance += bet * 2
            elif slot_random[0] == '🍒':
                balance += bet * 3
            elif slot_random[0] == '🎲':
                balance += bet * 4
            elif slot_random[0] == '💎':
                balance += bet * 10
            print(f'your balance: ${balance}')
        else:
            print('you lose')
            print(f'your balance: ${balance}')
        ask = input('do you want to play again (Y/N): ').upper()
        if ask == 'Y':
            continue
        elif ask == 'N':
            is_running = False


print(main())