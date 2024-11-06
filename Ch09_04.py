def unique_words(filename):
    # Initialize an empty set to store unique words
    unique_words = set()

    # Open the file and read its contents
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split line into words
            words = line.split()
            # Add each word to the set (duplicates automatically ignored)
            for word in words:
                # Remove punctuation and convert to lowercase for consistency
                cleaned_word = word.strip(",.!?\"':;").lower()
                if cleaned_word:  # Avoid adding empty strings
                    unique_words.add(cleaned_word)

    # Display the list of unique words
    print("Unique words in the file:")
    for word in sorted(unique_words):  # Sort for easier reading
        print(word)

# Specify the filename
filename = 'input.txt'  # Replace with your file path if necessary
unique_words(filename)
