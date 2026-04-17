'''
Function key_value that counts each character excluding spaces.
'''

def key_value(sentence):
    d = {}
    for c in sentence:
        if c != " ":
            d[c] = d.get(c, 0) + 1
    return d

text = input("Enter a sentence: ")
print(key_value(text))
