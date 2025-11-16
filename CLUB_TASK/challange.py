# 11. Count character frequency in a string
text = "hello world"
freq = {}
for ch in text:
    if ch != " ":
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
print("Character frequency:", freq)

# 12. Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {}
for key in original:
    value = original[key]
    swapped[value] = key
print("Swapped dictionary:", swapped)

# 13. Word → length dictionary
sentence = "Python is fun to learn"
words = sentence.split()
word_lengths = {}
for word in words:
    word_lengths[word] = len(word)
print("Word lengths:", word_lengths)

# 14. Print keys with even values
data = {"x": 10, "y": 15, "z": 22}
for key in data:
    if data[key] % 2 == 0:
        print("Even value key:", key)

# 15. Subjects with marks ≥ 40
marks = {"Math": 85, "English": 38, "Science": 72}
for subject in marks:
    if marks[subject] >= 40:
        print("Passed subject:", subject)