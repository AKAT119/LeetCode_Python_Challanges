str_sample = 'Azin Kati'

def reverse_st(s):
    result = ''
    for char in s:
        result = char + result
    return result


print(reverse_st(str_sample))
 