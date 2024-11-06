# Function to read a file and return a set of words
def read_words_from_file(filename):
    words_set = set()
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()  
            words_set.update(words)  
    return words_set

# Function to compare two files and display the requested comparisons
def compare_files(file1, file2):
    # Read words from both files
    words_file1 = read_words_from_file(file1)
    words_file2 = read_words_from_file(file2)

    # unique words in both files
    unique_words = words_file1 | words_file2  
    print("Unique words in both files:")
    print(sorted(unique_words))
    
    # words that appear in both files
    common_words = words_file1 & words_file2 
    print("\nWords that appear in both files:")
    print(sorted(common_words))
    
    # words that appear in the first file but not the second
    only_in_file1 = words_file1 - words_file2  
    print("\nWords that appear in the first file but not the second:")
    print(sorted(only_in_file1))
    
    # words that appear in the second file but not the first
    only_in_file2 = words_file2 - words_file1  
    print("\nWords that appear in the second file but not the first:")
    print(sorted(only_in_file2))
    
    # words that appear in either file but not both
    either_but_not_both = words_file1 ^ words_file2  
    print("\nWords that appear in either file but not both:")
    print(sorted(either_but_not_both))

# Specify the filenames
file1 = 'file1.txt'  # Replace with your first file path
file2 = 'file2.txt'  # Replace with your second file path

compare_files(file1, file2)
