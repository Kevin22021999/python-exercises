print("Welcome to your encryption program!")
print("Please enter your values first:")
#The user is introducted.

key = int(input("Key: "))
character = input("Character: ")
#The user is asked to input his key and character

print(f"Please remember the key {key} and your character {character}.")

encrypted_text = ""

for i in range(0, len(character)):
    ordinal_number = ord(character[i]) - key
    encrypted_character = chr(ordinal_number)
    encrypted_text = encrypted_text + encrypted_character


print(f"{character} becomes {encrypted_text}.")
#With the Caesar method, the character is transformed into another one.
