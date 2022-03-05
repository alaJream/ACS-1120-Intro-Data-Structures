import sys
import random

if len(sys.argv) < 2:
    sys.exit(0)

words = None

print(sys.argv)
words = []
if len(sys.argv) == 2:
    file_name = sys.argv[1]
    
    with open(file_name, 'r') as f:
        source = f.read().lower()
        split_source = source.split()
        
        for word in split_source:
            clean_word = word.strip("""'",♪..:--"?!();""")
            words.append(clean_word)
        # print(words)
else: 
    words = sys.argv[1:]

random.shuffle(words)

print(words[0])

