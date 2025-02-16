#write a Python list comprehension to create a new list containing only the prime numbers from the original list.



def isPrime(a):
  
    primes = [num for num in numbers if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    print(primes)  # Output: [23, 53, 71]





numbers = [10, 15, 23, 42, 53, 60, 71]
# Expected output: [23, 53, 71]
print(isPrime(numbers))