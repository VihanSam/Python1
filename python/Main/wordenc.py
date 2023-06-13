#User input
message = input("Enter a message")
message = message.upper()
output = ""
#for loop
for x in message:
    if x.isupper():
        value = ord(x)+3
        x = chr(value)

        if not x.isupper():
            value = value-26
            x = chr(value)
    output = output + x
print("Output Message: ", output)
#NEW
decode = ""
#for loop
for x in output:
    if x.isupper():
        value = ord(x)-3
        x = chr(value)

        if not x.isupper():
            value = value+26
            x = chr(value)
    decode = decode + x
print("Decoded message: ", decode)
