message = input("Enter a letter")
message = message.upper()
if message.isupper():
    value = ord(message)+3
    letter = chr(value)

if not letter.isupper():
    value = value-26
    letter = chr(value)
print("Output Message: ", letter)