import random

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]|;:',.<>?/`~✓✔✗★☆❤→←↑↓∞∆≠≈µ"
chars_list = list(chars)
random_chars_list = random.sample(chars_list, len(chars_list))
print(chars_list)
print(random_chars_list)

user_inp = input('enter something: ')
result = ""

for i in user_inp:
    if i in chars_list:
        index = chars_list.index(i)
        result += random_chars_list[index]
    else:
        result += i

print(result)