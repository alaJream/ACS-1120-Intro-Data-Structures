def read_file(filename):
    f = open(filename, 'r', encoding='utf-8-sig')
    words = f.read()
    f.close()
    return words

def histogram(file):
    with open(file, 'r') as f:
        text = f.read().split()
        punctuation = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥\n'''
        histogram = {}

        for word in text:
            for letter in word:
                if letter in punctuation:
                    word = word.replace(letter, "")
            if word in histogram.keys():
                histogram[word] += 1
            else:
                histogram[word] = 1
        return histogram

def unique_words(histogram):
    print("This text contains [" + str(len(histogram)) + "] unique words.")
    return len(histogram)

def frequency(word: str, histogram):
    if type(histogram) == dict:
        return histogram[word]
    else:
        for pair in histogram:
            if pair in histogram:
                if pair[0] == word:
                    return pair[1]

if __name__ == '__main__':
    file = ""
    histogram = histogram('sjack.txt')
    print(histogram)