import sys
import random



def read_words():
    with open('/usr/share/dict/words') as words_file:
        words = words_file.readlines()
        return words


def print_random(words, num_to_print):
    selected_words = random.choices(words, k=num_to_print)
    for word in [line.strip('\n') for line in selected_words]:
        print(word, end=" ")
    print('')

if __name__ == "__main__":
    words = read_words()
    print_random(words, int(sys.argv[1]))