def count_words_in_file(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    most_common_word = max(word_counts, key=word_counts.get)
    highest_count = word_counts[most_common_word]
    print(f"The most common word is '{most_common_word}' with {highest_count} occurrences.")
file_path = 'example.txt'  
count_words_in_file(file_path)