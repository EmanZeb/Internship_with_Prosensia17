line_of_text = input("Enter a line of text: ")
words = line_of_text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("Word counts:", word_counts)