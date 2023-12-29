# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def divisible_nums(input_number):

    divisble_nums = set()

    if input_number > 1:
        for i in range(1, input_number + 1):
            if input_number % i == 0:
                divisble_nums.add(input_number / i)
    
    return divisble_nums

def is_prime(input_number):

    if len(divisible_nums(input_number)) == 2:
        return True
    
    return False
    
def are_relatively_prime(first_num, second_num):

    first_divisible = divisible_nums(first_num)
    second_divisible = divisible_nums(second_num)

    if first_divisible.intersection(second_divisible) == {1}:
        return True
    
    return False

def primes(positive_int):

    prime_nums = []

    for i in range(positive_int + 1):
        if is_prime(i):
            prime_nums.append(i)

    return prime_nums

def prime_decomposition(positive_int):

    prime_decomp = []
    prime_nums = primes(positive_int)

    while positive_int != 1:
        for num in prime_nums:
            if positive_int % num == 0:
                positive_int /= num
                prime_decomp.append(num)

    prime_decomp = sorted(prime_decomp)

    return prime_decomp

if __name__ == "__main__":

    print(is_prime(0))
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(51))
    print(is_prime(113))

    print(are_relatively_prime(1, 2))
    print(are_relatively_prime(4, 9))
    print(are_relatively_prime(9, 64))
    print(are_relatively_prime(54, 113))

    print(primes(2))
    print(primes(10))
    print(primes(25))
    print(primes(50))

    print(prime_decomposition(6))
    print(prime_decomposition(10))
    print(prime_decomposition(20))
    print(prime_decomposition(54))