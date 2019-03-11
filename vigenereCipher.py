import numpy as np
import string
from collections import Counter

# This script calculates the length of keyword and output the key, decrypt the cipher by Vigenere Ciphere
# this function calculates the values I_c(y_i) for the given m
def find_index_coin(message, m):
    n = int(len(message) / m)
    substrs = divide_text(message, m)
    print(substrs)
    indexcoin = dict()
    for i in range(m):
        d = Counter(substrs[i])
        sum = 0
        for item, ct in d.items():
            print('%s occured %d times' % (item, ct))
            sum += ct * (ct - 1)
        indexcoin[i] = sum / (len(substrs[i]) * (len(substrs[i]) - 1))
    return indexcoin


# this function guesses the keyword length m as 1,2,3,4,...
# and then use statistical tests given before to check which
# guess looks good.
def recover_key_length(message):
    for i in range(1, len(message) + 1):
        val = find_index_coin(message, i)
        for key in val:
            if val[key] - 0.065 >= 0:
                return len(val)


# this function creates m substrings of y, denoted y1, y2, ..., ym;
def divide_text(message, m):
    substrings = ["" for x in range(m)]
    n = int(len(message) / m)
    r = len(message) % m
    i = 0
    while i < n:
        for j in range(m):
            substrings[j] += message[i * m + j]
        i += 1
    for x in range(r):
        substrings[x] += message[i * m + x]
    return substrings


# Assume the m we found is right, this function use the method discussed in the class to determine the actual key K
def find_key(message, m):
    p = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075,
         0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
    p = np.transpose(p)
    substrs = divide_text(message, m)
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q = np.zeros((m, 26))
    for i in range(m):
        for j in range(len(alpha)):
            ct = substrs[i].count(alpha[j])
            q[i, j] = ct / len(substrs[i])
    table = np.zeros((m, 26))
    keys = []
    for j in range(m):
        mglist = []
        for i in range(len(alpha)):
            vg = np.roll(q[j], (26 - i), axis=0)
            Mg = np.dot(p, vg)
            mglist.append(Mg)
        table[j, :] = mglist
        maxindex = mglist.index(max(mglist))
        keys.append(maxindex)
    return keys, table


# this function decrypts the cipher text by using the key we found
def vigenere_decoder(message, keyword):
    translated = ''
    message = message.lower()
    i = 0
    while i < len(message):
        for val in keyword:
            position = string.ascii_lowercase.index(message[i])
            position = (position - val) % 26
            translated += string.ascii_lowercase[position]
            i += 1
    return translated

ci_text = "XCIUIHTVOQVRLHJEYJXAVICEJFWXRVRUAAEPVPNEQLFZGFQEBXOIUXGIVJXVGLBRBXYIDBFZVKCSGHNITYJBXTSWXZHWZAYSEPINIIZ" \
          "WBRMITIFMQJRKLKASRIMIJPICEMIGGEIINWUTPZWVIFFEDRJXJXEHTISVNGOWRRVLIMZZGWLHZWZKFXHDRRASRXCEKKAOINYJIJLWJP" \
          "VGGGXMSCSNXVVGTIKLXJXYIAKHVXREKTVZWLPLEERIEJGKGZQVRLBWNSDILBQZWLRSUPZXFVWVSQIIXZXGJRKIFMSAICIUMVJRZGUHQ" \
          "HYEMUTXDSEWXKSHXYILXGCRFPGZCKVFZAWIMIMIFBRMIJTGGWZXFEUHYMXFVVXVJVUYDREPXYSJBDZHNEJKEIXZWKNIYFPEXXHZVRPB" \
          "NHBIWSJXBVQGPWFEICTSEFYIMTELBSIWJIJOMXIJRGPIIGICHMGZVKEAGGJQDYFBGVXZSFLFTHVJSNPOAZXZMLZOVCFXGZWJEJRXJHV" \
          "GJRTOXYIUHQHYEMUTXDSEWKHPZPPMFMLZLRRVLSAXYIWGHPWVVLAMNEGTDBINFFXZPLZRKLWWEOEZWAGQJXZSFHZZVVPWVXMSEMUGIO" \
          "AFVCLSMEKVWLXJRRRWEIXXISFBGYIMMUXMAXYIUHQHYEMUTXDSEWHKSQMUIJBWNIIZWWADXYEOTVMEEXKXIFMEKLASNITSEFYIMTELB" \
          "SIWKLWIVJZZHWKGVRESLIVJZZHWMLZHRXSUIXELWWBXCEJHWLMBRVHLAIOITLFHPJKPWMVLOLRXAMGVRESLUIVGTIKLIYFPEFRXCMIH" \
          "HTVOCNIVHRJXYENXEICJMDOIMFLPDXXNEEHLAIYMJGMLWDSEWOBXCMEXZXISITYLBZZFIEFVLVVVWLBPGSEKGBRBAYMDXXCIIIZTWIS" \
          "KCWMFZIEEVXGDWZSFPLZXYIJMSNIVODXKDWCELBSIAVQMLXRSIOOBXCGFRYKINWZRVNWOVPEUTHZQZGKIVDZRGQZVJYGWSGHJXYIJLX" \
          "JGIEXMEIEGTJHEXLKLSMEYHIIKLINECPGYXCIDYDMMKPVGGFTZXZRYVSIGVVFLXCEKLSOIWIVRLAIASTYKHJNSDYUAHZFRXWUYOAVGS" \
          "GEGPRKJXIOLRXOXADPCRWXHJRXSAGKCSEIKMEIHZRXHVHIUTMUPDGUITTXZESSMMLJASIKMXJTISLXGOPZFWKXTEEHKXGPVZXQBRWSK" \
          "LGNVGENWSGHJYIXWVLISCSYR"


for count in range(4, 9):
    print("If m = %d, the index of coincidence for each substring are" % count)
    # It outputs a dictionary where each key i matches to a index of coincidence for y_i
    print(find_index_coin(ci_text, count))
key, matrix = find_key(ci_text, 7)
translated_key = ""
for v in key:
    translated_key += string.ascii_lowercase[v]
print("The keyword is ")
print(key)
print(translated_key)
matrix = np.transpose(matrix)
s = [[str(e) for e in row] for row in matrix]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
sub_table = [fmt.format(*row) for row in s]
print('\t'.ljust(21).join(['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7']))
print('\n'.join(sub_table))
# this plain text variable contains the text without any space or period
plain_text = vigenere_decoder(ci_text, key)

text = 'the department of justice has been and will always be committed to protecting the liberty and security of ' \
       'those whom we serve. in recent months however we have on a new scale seen mainstream products and services' \
       ' designed in a way that gives users sole control over access to their data. as a result law enforcement' \
       ' is sometimes unable to recover the content of electronic communications from the technology provider even in ' \
       'response to a court order or duly authorized warrant issued by a federal judge. for example many ' \
       'communications services now encrypt certain communications by default with the key necessary to decrypt ' \
       'the communications solely in the hands of the end user. this applies both when the data is in motion over' \
       ' electronic networks or at rest on an electronic device. if the communications provider is served with ' \
       'a warrant seeking those communications the provider cannot provide the data because it has designed' \
       ' the technology such that it cannot be accessed by any third party. we do not have any silver bullets' \
       ' and the discussions within the executive branch are still ongoing. while there has not yet been a ' \
       'decision whether to seek legislation we must work with congress industry academics privacy groups and ' \
       'others to craft an approach that addresses all of the multiple competing concerns that have been' \
       ' the focus of so much debate. but we can all agree that we will need ongoing honest and informed public' \
       ' debate about how best to protect liberty and security in both our laws and our technology.'
print(text)
