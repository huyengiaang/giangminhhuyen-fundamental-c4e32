# find all prime numbers from 2 to 100
from prime_number import iss_prime

for k in range(2,100):
    if iss_prime(k):
        print(k)