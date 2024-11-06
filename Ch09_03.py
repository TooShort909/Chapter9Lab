# Dictionary to assign codes to each letter
codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '$',
    'D': '^', 'd': '&', 'E': '*', 'e': '(', 'F': ')', 'f': '-',
    'G': '_', 'g': '=', 'H': '+', 'h': '[', 'I': ']', 'i': '{',
    'J': '}', 'j': '|', 'K': ';', 'k': ':', 'L': '"', 'l': '<',
    'M': '>', 'm': ',', 'N': '.', 'n': '/', 'O': '?', 'o': '`',
    'P': '~', 'p': '1', 'Q': '2', 'q': '3', 'R': '4', 'r': '5',
    'S': '6', 's': '7', 'T': '8', 't': '0', 'U': 'a', 'u': 'b',
    'V': 'c', 'v': 'd', 'W': 'e', 'w': 'f', 'X': 'g', 'x': 'h',
    'Y': 'i', 'y': 'j', 'Z': 'k', 'z': 'l', ' ': '|'
}

# Encryption function
def encrypt_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        text = infile.read()
        encrypted_text = ""
        for char in text:
            encrypted_text += codes.get(char, char)  # Use code if available, otherwise keep char
        outfile.write(encrypted_text)
    print("File encrypted successfully.")

# Encrypt the contents of 'input.txt' to 'encrypted.txt'
encrypt_file('input.txt', 'encrypted.txt')

# Reverse the dictionary to create a decryption map
decodes = {v: k for k, v in codes.items()}

# Decryption function
def decrypt_file(encrypted_filename):
    with open(encrypted_filename, 'r') as infile:
        encrypted_text = infile.read()
        decrypted_text = ""
        for char in encrypted_text:
            decrypted_text += decodes.get(char, char)  # Use original if char not in decodes
        print("Decrypted content:")
        print(decrypted_text)

# Decrypt and display the contents of 'encrypted.txt'
decrypt_file('encrypted.txt')
