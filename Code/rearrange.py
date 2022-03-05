import random

def word_shuffler(word_list):
    set_list = word_list.split()
    print(f"Given words: {set_list}")
    shuffled_list = random.sample(set_list, len(set_list))
    return shuffled_list

if __name__ == '__main__':
    word_list = input('Insert word list: ')
    new_sentence = word_shuffler(word_list)
    print(f'Given list: {word_list}')
    print(f'Shuffled list: {new_sentence}')

