numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number > 1:
        for i in range(number):                  # на себя не делим
            is_prime = True
            if i > 1 and number % i == 0:        # делим от 2
                is_prime = False
                break
        if is_prime == True:
            primes.append(number)
        else:
            not_primes.append(number)
print("Primes=", primes)
print("Not Primes=", not_primes)