numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
i = 0
len_numbers = len(numbers)
while i < len_numbers:
    number = numbers[i]
    if number > 1:
        is_prime = True
        j = 2
        while j < number:                   # на себя не делим
            if number % j == 0:             # делим от 2
                is_prime = False
                break
            j += 1
        if is_prime == True:
            primes.append(number)
        else:
            not_primes.append(number)
    i += 1
print("Primes=", primes)
print("Not Primes=", not_primes)