import string

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # Convert text to lowercase
    char_count = {}

    for char in text:
        if char.isalpha():  # Only count letters (ignore spaces, punctuation, numbers)
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count  # Return only alphabetic character counts

def print_report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Convert dictionary to sorted list of tuples (char, count), sorted by count descending
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    # Print character frequencies in required format
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print_report(word_count, char_count)  # Call function to print report

main()
