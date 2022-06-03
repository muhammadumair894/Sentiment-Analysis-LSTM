#1) Load in and visualize the data
# read data from text files
with open('ENG_StopSuspending_Pakistani.txt', 'r', encoding='utf-8') as f:
 reviews = f.read()

print()
print(reviews)

#2) Data Processing — convert to lower case
reviews = reviews.lower()

#3) Data Processing — remove punctuation
from string import punctuation
print(punctuation)
all_text = ''.join([c for c in reviews if c not in punctuation])

#4) Data Processing — create list of Tweets

reviews_split = all_text.split('\n')
print ('Number of reviews :', len(reviews_split))

#5) Tokenize — Create Vocab to Int mapping dictionary

from collections import Counter
all_text2 = ' '.join(reviews_split)
# create a list of words
words = all_text2.split()
# Count all the words using Counter Method
count_words = Counter(words)

total_words = len(words)
sorted_words = count_words.most_common(total_words)
print (count_words)

vocab_to_int = {w:i for i, (w,c) in enumerate(sorted_words)}

print (vocab_to_int)

#6) Tokenize — Encode the words

reviews_int = []
for review in reviews_split:
    r = [vocab_to_int[w] for w in review.split()]
    reviews_int.append(r)
print (reviews_int[0:3])



