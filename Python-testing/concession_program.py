# concession stand program

menu = {
    'hot dog': 3.50,
    'potato': 2.00,
    'soda': 1.50,
    'lemonade': 2.50,
    'pizza': 4.00,
    'hamburder': 4.00,
}
cart = [
    # generated user
]
total = 0

menu_keys = list(menu.keys())
menu_values = list(menu.values())
print('---------------Menu---------------')
i = 0
while i < len(menu):
    print(f'{menu_keys[i]:14} {menu_values[i]:.2f}')
    i += 1
print('----------------------------------')

while True:
    food = input(' (q to quit) Enter food: ').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print('---------------Cart---------------')
print(', '.join(cart))
i = 0
while i < len(cart):
    total += menu.get(cart[i])
    i += 1
print(f'Total: ${total:.2f}')
print('----------------------------------')