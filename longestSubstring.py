#Write a Python function to find the 
#longest substring in a given string that contains no repeating characters.

#condition : not duplicate

def longest_unique_substring(strg_smpl):
    l = 0 # pointer left , r the pointer right 
    char_set = set()
    longest = 0
    len_str =  len(strg_smpl)
    for r in range(len_str):
        while strg_smpl[r] in char_set:
            char_set.remove(strg_smpl[l])
            l+=1
        char_set.add(strg_smpl[r])
        len_window = (r - l) + 1
       # longest = max(longest, len_window)
        if len_window > longest:
            longest = len_window
            start_index = l  # Update the start of the longest substring

    # Extract the longest substring using the starting index and length
    longest_substring = strg_smpl[start_index:start_index + longest]
    return longest, longest_substring



# Test cases
print(longest_unique_substring("abcabcbb"))  # Output: "abc"
print(longest_unique_substring("bbbbb"))     # Output: "b"
print(longest_unique_substring("pwwkew"))    # Output: "wke"



     
