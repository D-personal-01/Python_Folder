# Decoding code for the encoded message

encoded = input("Enter encoded message: ")
encoded = encoded[:-1]

decoded = ""
i = 0
even = True

while i < len(encoded):
    if even:
        decoded += chr(ord(encoded[i]) - 17)
        i += 1
    else:
        num = ""
        while encoded[i] != "z":
            num += encoded[i]
            i += 1

        ascii_val = round((int(num) - 1650) ** (1/3))
        decoded += chr(ascii_val)
        i += 1  

    even = not even

print(decoded)