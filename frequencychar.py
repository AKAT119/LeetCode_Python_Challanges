from collections import Counter

def char_frequency(s):
    return dict(Counter(s))


Strr= 'Azin Katioii'
print(char_frequency(Strr)) 