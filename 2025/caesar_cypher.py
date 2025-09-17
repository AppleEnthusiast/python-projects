print("Welcome to the Caesar Cipher!")
print("This program shifts letters by 3 positions in the alphabet.\n")

text = input("Enter a message: ")
shifted_text = ""

for char in text:
    if char.isalpha():  # only shift letters
        # Convert to number
        code = ord(char)

        # Shift uppercase letters
        if char.isupper():
            code = (code - ord('A') + 3) % 26 + ord('A')

        # Shift lowercase letters
        elif char.islower():
            code = (code - ord('a') + 3) % 26 + ord('a')

        # Convert number back to character
        shifted_text += chr(code)
    else:
        # Leave spaces/punctuation unchanged
        shifted_text += char

print("\nEncrypted message:")
print(shifted_text)

