import argparse
import sys
import re
import collections


def sort_words_by_frequency(words_frequency):
    return sorted(words_frequency, key=lambda i: i[1], reverse=True)


def count_most_common_words(text, words_count):
    pattern = re.compile(r'[-.?!,/()\'\":;]')
    formated_text = re.sub(pattern, '', text)

    all_words_list = formated_text.split()
    unique_words_list = list(set(all_words_list))
    words_counter = collections.Counter(all_words_list)
    words_frequency = {word:words_counter[word] for word in unique_words_list}
    words_frequency = list(words_frequency.items())

    sorted_words_frequency = sort_words_by_frequency(words_frequency)

    return sorted_words_frequency[:words_count]


def print_results(words_frequency):
    for item in words_frequency:
        print(f'{item[0]}: {item[1]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Finding a most common words')
    parser.add_argument('file', metavar='Path', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='path to file that will parse')
    parser.add_argument('number_to_display', metavar='N', nargs='?', type=int, help='number of the most common words to display')
    
    args = parser.parse_args(['./text.txt', '10'])
    # args = parser.parse_args()

    text = args.file.read().lower()
    args.file.close()

    words_frequency = count_most_common_words(text, args.number_to_display)
    print_results(words_frequency)
