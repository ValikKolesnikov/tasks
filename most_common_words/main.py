import argparse
import sys
import re
import collections


def sort_words_by_frequency(words_frequency):
    return sorted(words_frequency, key=lambda i: i[1], reverse=True)


def count_most_common_words(text, words_count):
    pattern = re.compile(r'[-.?!,/()\'\":;]')
    formated_text = re.sub(pattern, '', text)

    words_counter = collections.Counter(formated_text.split())
    return words_counter.most_common(words_count)

def print_results(words_frequency):
    for item in words_frequency:
        print(f'{item[0]}: {item[1]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Finding a most common words')
    parser.add_argument('file', metavar='Path', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='path to file that will parse')
    parser.add_argument('number_to_display', metavar='N', nargs='?', type=int, help='number of the most common words to display')
    
    args = parser.parse_args()

    text = args.file.read().lower()
    args.file.close()

    words_frequency = count_most_common_words(text, args.number_to_display)
    print_results(words_frequency)
