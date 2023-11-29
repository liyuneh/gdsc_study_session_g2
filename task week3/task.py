def get_paragraph():
    text = input("Please enter a paragraph of text: ")
    return text

def tokenize_text(text):
    words = text.split()
    return words

def calculate_word_frequency(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def display_word_frequencies(word_freq):
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    for word, freq in sorted_word_freq:
        print(f"Word: {word}, Frequency: {freq}")

def display_top_n_words(word_freq, n):
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:n]
    for word, freq in sorted_word_freq:
        print(f"Word: {word}, Frequency: {freq}")

def search_word_frequency(word_freq, word):
    if word in word_freq:
        print(f"The word '{word}' appears {word_freq[word]} times.")
    else:
        print(f"The word '{word}' is not found in the text.")

def find_longest_word(words):
    longest_word = max(words, key=len)
    return longest_word

def calculate_average_word_length(words):
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length


user_text = get_paragraph()


tokenized_words = tokenize_text(user_text)


word_frequencies = calculate_word_frequency(tokenized_words)


display_word_frequencies(word_frequencies)

n = int(input("Enter the value of N for top N words: "))
display_top_n_words(word_frequencies, n)

search_word = input("Enter a word to search for its frequency: ")
search_word_frequency(word_frequencies, search_word)


longest_word = find_longest_word(tokenized_words)
print(f"The longest word in the text is: {longest_word}")

average_word_length = calculate_average_word_length(tokenized_words)
print(f"The average word length in the text is: {average_word_length}")
