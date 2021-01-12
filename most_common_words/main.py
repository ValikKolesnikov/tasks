def format_string(string):
    if string:
        for char in string:
            if not char.isalpha() and not char == ' ':
                string = string.replace(char, '')
        return string
    return ''


def get_text_from_file(path_to_file):
    try:
        with open(path_to_file, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print('File not found')
        return ''
    except IsADirectoryError:
        print('Excepted file but was given directory')
    return text.lower()



def sort_words_by_frequency(words_frequency):
    return sorted(words_frequency, key=lambda i: i[1], reverse=True)



def count_most_common_words(text, words_count):
    formated_text = format_string(text)
    words_list = formated_text.split()
    words_frequency = {i:words_list.count(i) for i in words_list}
    words_frequency = list(words_frequency.items())

    sorted_words_frequency = sort_words_by_frequency(words_frequency)

    return sorted_words_frequency[:words_count]


def print_results(words_frequency):
    for i in words_frequency:
        print(f'{i[0]}: {i[1]}')


if __name__ == '__main__':
    path_to_file = input('Enter path to file\n')
    try:
        output_words_number = int(input('Enter a number of the most common words to display\n'))
    except ValueError:
        print('Value error: given string but excepted int')
        output_words_number = 1
    text = get_text_from_file(path_to_file)
    words_frequency = count_most_common_words(text, output_words_number)
    print_results(words_frequency)
