text = input('Enter text: ').lower()
if any(char.isdigit() for char in text):
    print("Error")
    exit()
shift_key_input = input('Enter shift_key: ')
if not shift_key_input.isdigit():
    print('wrong key')
    exit()
shift_key = int(shift_key_input)

words = 'abcdefghijklmnopqrstuvwxyz'
words_list = list(words)
text_controller = list(text)

index_list = []
result = ''
i = 0
while i < len(text_controller):
    if text_controller[i] == ' ':
        result += ' '
        index_list.append(' ')
    else:
        index = words_list.index(text_controller[i])
        index_list.append((index + shift_key) % 26)
        result += words_list[(index + shift_key) % 26]
    i += 1


print(index_list)
print(result)