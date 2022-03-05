import random

from dictogram import Dictogram


class MarkovChain(dict):

    def __init__(self, words):
        super(MarkovChain, self).__init__()
        self.corpus = words

    def create_chain(self, order=2):
        for index, word in enumerate(self.corpus):
            try:
                key = []
                for i in range(0, order):
                    key.append(self.corpus[index + i])

                key = tuple(key)
                value = self.corpus[index + order]
                if key in self:
                    self[key].add_count(value)
                else:
                    self[key] = Dictogram([value])
            except IndexError:
                break

    def walk(self, max_length=200):
        words = []
        keys = list(self)

        current_key = random.choice(keys)  # Random first key
        while max_length > len(words):
            try:
                next_word = self[current_key].sample()
                words.append(next_word)

                next_key = list(current_key)
                next_key.pop(0)
                next_key.append(next_word)

                current_key = tuple(next_key)
            except KeyError:
                break 
        return " ".join(words)


if __name__ == "__main__":
    source_file = open("sjack.txt")
    file_contents = source_file.read()

    chain = MarkovChain(file_contents.split())

    chain.create_chain(3)
    print(chain.walk(100))