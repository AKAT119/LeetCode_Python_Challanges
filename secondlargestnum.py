import numpy as np

a =  [18, 1, 3, 10, 4, 6, 9, 8, 11, 10]

def second_largest(a):
    unique_nume = list(set(a))
    unique_nume.sort()
    return unique_nume[-2] if len(unique_nume) >= 2 else None





print(second_largest(a))  # Output: 10
