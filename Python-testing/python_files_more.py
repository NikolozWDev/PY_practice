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
new_file_about = 'Get methods and more features'

with open(new_file, 'w') as file:
    file.write(new_file_about)
    print(f'{new_file} was created')