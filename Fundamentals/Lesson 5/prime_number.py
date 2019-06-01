# check if n is a prime number
n = 15
is_prime = True
for v in range(2,n):
    if n % v == 0:
        is_prime = False
        # print(n, "is not a prime number.")
        # uoc.append(v)
if is_prime:
    print(n, 'is a prime number.')
else:
    print(n, 'is not a prime number.')




# another way
def iss_prime(n):
    for v in range (2,n):
        if n % v == 0:
            return False
    return True

print(iss_prime(113))

# find all prime numbers from 2 to 100 
for k in range(2,100):
    if iss_prime(k):
        print(k)
