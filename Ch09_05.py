def display_word_frequencies(filename):
    # Initialize an empty dictionary to store word frequencies
    word_counts = {}

    # Open the input file and read its contents
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            words = line.split()
            # Count each word
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

    # Display the word frequencies on the screen
    print("Word frequencies in the file:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")


filename = 'input.txt'  # Replace with your file path if necessary

display_word_frequencies(filename)
