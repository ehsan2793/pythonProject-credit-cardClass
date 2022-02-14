
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(text,shift))

    again = input("Type 'yes' to continue otherwise type 'no'. \n")
    should_continue = True if again == 'yes' else False



# def encrypt(text,shift)-> str:
#     res = []
#     for i in text:
#         index = alphabet.index(i)
#         new_position = index + shift
#         if new_position > 25:
#             new_position = new_position % 26
#         res.append(alphabet[new_position])
#
#     return "".join(res)
#
#
# def decrypt(text,shift):
#     res = []
#     for i in text:
#         index = alphabet.index(i) - shift
#         if index < 0:
#             index  = 26 - (-index)
#         res.append(alphabet[index])
#
#     return "".join(res)



# if direction  == 'encode':
#     print(encrypt(text,shift))
# elif direction == 'decode':
#     print(decrypt(text,shift))


def caesar(text, shift):
    res = []
    if direction == "decode":
        shift *= -1
        if shift < 0:
            shift = 26 + shift
    for char in text:
        if char not in alphabet:
            res.append(char)
            continue
        position = alphabet.index(char)
        new_position = (position + shift) % 25
        res.append(alphabet[new_position])

    return "".join(res)
