'''
This program finds all prime numbers in a range and prints count and sum.
'''

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

start = int(input("Start of range: "))
end = int(input("End of range: "))

primes = [num for num in range(start, end+1) if is_prime(num)]

print("Prime numbers:", primes)
print("Count:", len(primes))
print("Sum  :", sum(primes))
