from collections import Counter
import re

def top_n_frequent_words(file_path, N):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            word_counts = Counter(words)
            return word_counts.most_common(N)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
print(top_n_frequent_words('romeo.txt', 3))