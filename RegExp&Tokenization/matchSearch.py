import re

with open("scene_one.txt", "r") as scene_text:
    scene_one = scene_text.read()
    
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentence = sent_tokenize(scene_one)

# 1st task
# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())
print("-----------------------------------")


# 2nd task
# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*\]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1, scene_one))
print("------------------------------------")

# 3rd task
# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w\s]+:"
print(re.match(pattern2, sentence[3]))