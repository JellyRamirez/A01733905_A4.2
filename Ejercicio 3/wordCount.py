"""
wordCount.py

This script identifies all distinct words and the frequency of them,
given a file cointaing words.
"""
import sys
import time

def read_file(file_path):
    """Reads the file and returns its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{file_path}'.")
        sys.exit(1)
    except OSError as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)

def count_words(text):
    """Counts the frequency of each distinct word in the text."""
    word_count = {}
    word = ""
    for char in text:
        if char.isalnum():
            word += char.lower()
        else:
            if word:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                word = ""
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_results(word_count, elapsed_time):
    """Writes the results to a file and prints them to the console."""
    output_file = "WordCountResults.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in sorted(word_count.items()):
            file.write(f"{word}: {count}\n")
            print(f"{word}: {count}")
        file.write(f"\nExecution time: {elapsed_time:.4f} seconds\n")
        print(f"\nExecution time: {elapsed_time:.4f} seconds")

def main():
    """Main function to handle command-line execution."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()
    text = read_file(file_path)
    word_count = count_words(text)
    elapsed_time = time.time() - start_time
    write_results(word_count, elapsed_time)

if __name__ == "__main__":
    main()
