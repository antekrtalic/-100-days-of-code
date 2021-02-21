def count_words(filename):
    """Count the approximate number of words in a file."""
    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_woman.txt']
    for filename in filenames:
        try:
            with open(filename, encoding="utf-8") as f:
                contents = f.read()
        except FileNotFoundError:
            pass
        else:
            # Count the approximate number of words in file.
            words = contents.split()
            num_words = len(words)
            print(f"The file {filename} has about {num_words} words.")

filename = "alice.txt"
count_words((filename))
