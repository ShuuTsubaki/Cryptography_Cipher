# Used to decrypt special permutation with mxn key
def decryptPermutation(message, m, n):
    translated = ''
    # Divides the cipher text to
    for i in range(m):
        for j in range(n):
            translated += message[j*m+i]
    return translated
# use example
val = 'nnogodmowdiirosnuncgnthoagiuleetotfxniixgnaxatmx'
print(decryptPermutation(val, 6, 8))
print(decryptPermutation(val, 8, 6))
print(decryptPermutation(val, 4, 12))
