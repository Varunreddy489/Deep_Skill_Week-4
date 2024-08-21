
from text_processing_tool import count_words, find_unique_words, convert_to_uppercase

def main():
    text = input("Enter a text string: ")
    
    # Count words
    num_words = count_words(text)
    print(f"Number of words: {num_words}")
    
    # Find unique words
    unique_words = find_unique_words(text)
    print(f"Unique words: {unique_words}")
    
    # Convert to uppercase
    uppercase_text = convert_to_uppercase(text)
    print(f"Text in uppercase: {uppercase_text}")

if __name__ == "__main__":
    main()
