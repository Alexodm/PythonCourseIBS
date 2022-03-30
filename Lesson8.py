def invert_txt_and_print(file_name):
    inverted_file_name = resolve_inverted_file_name(file_name)

    with open(file_name, 'r') as f:
        print(f.read())

    with open(file_name, 'r') as f:
        symbol_list = list(f.read())

    with open(inverted_file_name, 'w') as f:
        f.write(''.join(symbol_list[::-1]))

    with open(inverted_file_name, 'r') as f:
        print(f.read())


def resolve_inverted_file_name(file_name):
    file_name_len = len(file_name)
    inv_file_name = file_name[:file_name_len - 4] + '_inverted.txt'
    print('Origin file name = ' + file_name)
    print('Inverted file name = ' + inv_file_name)
    return inv_file_name


invert_txt_and_print('Lesson8_text_file.txt')
