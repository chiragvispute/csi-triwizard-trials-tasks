def caesar_cipher_encrypt(text, shift):
    # TODO: Write logic here
    return text

def main():
    # Take input
    text = input("Enter a string: ")
    shift = int(input("Enter shift value: "))

    # Call the function
    result = caesar_cipher_encrypt(text, shift)

    # Print the result
    print("Encrypted text:", result)

if __name__ == "__main__":
    main()
