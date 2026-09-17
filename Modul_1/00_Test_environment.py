print("Welcome to your decryption program")
print("Please enter your Key and character")
#Welcomes and introducts the customer
key = int(input("key: "))
character = input("Character: ")
#Asks for the key and character that is stored in variables

decrypted_text = ""
# This is very important because we create an empty string to store the decrypted text.
# Without this, Python would give an error on line 16 because it would try to add
# a new character to a variable that has not been created yet.

for i in range(0, len(character)):
    ordinal_number = ord(character[i]) + key
    decrypted_character = chr(ordinal_number)
    decrypted_text = decrypted_text + decrypted_character
# This loop goes through the encrypted text one character at a time.
# `i` starts at 0 and increases until the last position in `character`.
# In each loop, one encrypted character is selected and converted into its ASCII value.
# The key is then added to shift the character back to its original position.
# After that, the new ASCII value is converted back into a readable character.
# Finally, the decrypted character is added to `decrypted_text` so the full word
# is built one letter at a time.

print(f"Your decrypted text/word is: {decrypted_text} ")