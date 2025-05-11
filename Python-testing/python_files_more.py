import os

# file detection
file_path = 'files/text.txt'

if os.path.exists(file_path):
    print(f'file "{file_path}" exists')
    if os.path.isfile(file_path):
        print(f'{file_path} is file')
    elif os.path.isdir(file_path):
        print(f'{file_path} is folder')
else:
    print(f'file {file_path} does not exists')



# writing files
new_file = 'files/new-file.txt'
new_file_about = "Computer programming"

with open(new_file, 'w') as file:
    i = 0
    while i < 10:
        file.write(new_file_about + "\n")
        i += 1
    print(f'{new_file} was created')


# reading files
reader_file = 'files/reading_file.txt'
reader_file_about = 'here is text'
with open(reader_file, 'w') as file:
    file.write(reader_file_about)
    print('file created')
try:
    with open(reader_file, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('file not found')
except PermissionError:
    print('you have not permission to read file')



import json

json_file = 'files/json_about.json'
employee = {
    'giorgi': 'job',
    'sandro': 'list',
    'stefane': 'arr'
}
with open(json_file, 'w') as file:
    json.dump(employee, file)
    print('created json file')
with open(json_file, 'r') as file:
    content = json.load(file)
    print(content)