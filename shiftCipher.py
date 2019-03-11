MAX_KEY_SIZE = 26
# a simple shift cipher decrypted script
def bruteforce(message):
    for i in range(MAX_KEY_SIZE):
        print(i, decryptedMessage(message, i))

def decryptedMessage(message, key):
    translated = ''
    key = -key
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

# val = 'scksnrokbdsckcrspdsxqcoksdgyevnlocydowzdsxqdytecdgbsdomkxiyerokbwoxyg'
t1 = 'scksnrokbdsckcrspdsxqcok'
t2 = 'sdgyevnlocydowzdsxqdytecdgbsdomkxiyerokbwoxyg'
bruteforce(t1)
print("the keyword is:")
print(decryptedMessage(t1, 10))
print('Your translated text is:')
print(decryptedMessage(t2, 10))