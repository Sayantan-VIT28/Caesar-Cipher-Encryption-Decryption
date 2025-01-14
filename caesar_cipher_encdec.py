def caesarcipher_encryption(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesarcipher_decryption(text, shift):
    return caesarcipher_encryption(text, -shift)

def main():
    print ("Caesar Cipher Encryption/Decryption Program!")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            print("Message to be encrypted:", message)
            shift = int(input("Enter the shift value: "))
            print("Shift value:", shift)
            encrypted_message = caesarcipher_encryption(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            print("Message to be decrypted:", message)
            shift = int(input("Enter the shift value: "))
            print("Shift value:", shift)
            decrypted_message = caesarcipher_decryption(message, shift)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()