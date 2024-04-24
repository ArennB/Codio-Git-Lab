import sys

def caesar_cipher(text, shift):
    encrypted_text = ""
    for character in text:
        if character.isalpha():
            shifted_value = (ord(character.upper()) - 65 + shift) % 26 + 65
            encrypted_text += chr(shifted_value)
    return encrypted_text

def print_encrypted_blocks(encrypted_text):
    for index in range(0, len(encrypted_text), 5):
        print(encrypted_text[index:index+5], end=' ')
    print()

def main():
    if len(sys.argv) != 2:
        print("Correct Usage: python3 unique_cipher.py <shift_number>")
        sys.exit(1)

    try:
        shift_amount = int(sys.argv[1]) % 26
    except ValueError:
        print("Shift value must be an integer.")
        sys.exit(1)

    print("Input text for encryption (Ctrl+D to end):")
    try:
        for line in sys.stdin:
            encrypted_line = caesar_cipher(line, shift_amount)
            print_encrypted_blocks(encrypted_line)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
