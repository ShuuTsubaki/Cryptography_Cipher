import string
# a simple script to decrypt affine cipher
def decryptMessage(message, keyA, keyB):
    translated = ''
    for symbol in message:
        position = string.ascii_lowercase.index(symbol)
        num = position * keyA + keyB
        num = num % 26
        translated += string.ascii_lowercase[num]
    return translated

val = 'cowcbfxiviagwiuxivixcdcbscbfxofrgbsrcafgnscttivcax'
print(decryptMessage(val, 21, 18))
