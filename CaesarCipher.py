# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""

    # loop through each character in the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

            # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # keep other characters unchanged
        else:
            result += char

    return result

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program to allow user input
def main():
    choice = input("Do you want to Encrypt or Decrypt? (E/D): ").upper()

    # Get user input for text and shift
    text  = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Perform  encryption or decryption based on user choice
    if choice == 'E':
        print("Encrypted message: ", encrypt(text, shift))

    elif choice == 'D':
        print("Decrypted message: ", decrypt(text, shift))

    else:
        print("Invalid choice. Please choose E for encryption or D for decryption.")

# Run the Caesar Cipher program
if  __name__ == "__main__":
    main()