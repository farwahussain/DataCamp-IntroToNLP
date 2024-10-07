#utilize word_tokenize and sent_tokenize from nltk.tokenize to tokenize both words and sentences from Python strings - in this case, the first scene of Monty Python's Holy Grail.

#file containing text for the first scene of Monty Python's Holy Grail
with open("scene_one.txt", "r") as scene_one:
    scene_text = scene_one.read()

# Import necessary modules
from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_text)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_text))

# Print the unique tokens result
print(unique_tokens)
