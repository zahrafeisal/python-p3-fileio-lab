def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode = 'w', encoding = 'utf-8') as file_name:
        file_name.write(file_content)
    pass

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode = 'a', encoding = 'utf-8') as file_name:
        file_name.write(append_content)
    pass

def read_file(file_name):
    with open(f'{file_name}.txt', encoding = 'utf-8') as file_name:
        return file_name.read()
    pass
