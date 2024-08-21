
def count_words(text: str) -> int:
    """
    Count the number of words in the given text.
    """
    words = text.split()
    return len(words)
