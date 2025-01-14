#Write a Python function to check if two strings are anagrams of each other.
#Two strings are anagrams if they contain the same characters in the same frequency, but in any order.
def compare_dics(str1, str2):
    def anagram_string(str_sample):
        frequency = {}
        for s in str_sample:
            if s in frequency:
                frequency[s]+=1
            else:
                frequency[s] = 1
        return frequency
    return anagram_string(str1) == anagram_string(str2)




str1 = 'listen'
str2 = 'silent'
print(compare_dics(str1,str2))