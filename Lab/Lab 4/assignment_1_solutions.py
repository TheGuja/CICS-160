import math

def is_prime(n):
    next_number_to_check = 2
    while (next_number_to_check <= math.sqrt(n)):
        if (n%next_number_to_check) == 0:
            return(False)
        next_number_to_check = next_number_to_check + 1
        
    return(True)

def are_relatively_prime(x, y):
    next_number_to_check = 2
    check_up_to = min(x,y)
    while (next_number_to_check <= check_up_to):
        if (x%next_number_to_check == 0 and y%next_number_to_check == 0):
            return(False)
    next_number_to_check = next_number_to_check +1

    return(True)

def primes(n): 
    next_number_to_try = 2
    list_to_return = []
    while (next_number_to_try <= n):
        if (is_prime(next_number_to_try)):
            list_to_return.append(next_number_to_try)
    next_number_to_try = next_number_to_try +1

    return(list_to_return)

def prime_decomposition(n):
    decomposition = []
    whats_left = n
    next_candidate = 2
    while (whats_left > 1):
        if (whats_left%next_candidate == 0 and is_prime(next_candidate)):
            decomposition.append(next_candidate)
            whats_left = whats_left/next_candidate
        else:
            next_candidate = next_candidate + 1
    
    return(decomposition)



# main program
if __name__ == '__main__':
    # candidate = int(input("Enter an integer: "))
    # if is_prime(candidate):
    # print (candidate, "is prime.")
    # else:
    # print (candidate, "is not prime")
    print("is 2 prime?", is_prime(2))
    # print("are 2 and 7 relatively prime?", are_relatively_prime(2,7))
    # print("are 2 and 8 relatively prime?", are_relatively_prime(2,8))
    # print("are 4 and 8 relatively prime?", are_relatively_prime(4,8))
    # print("are 10 and 9 relatively prime?", are_relatively_prime(10,9))
    # print("prime numbers up to 7:", primes(7))
    # print("prime numbers up to 10:", primes(10))
    # print("prime numbers up to 2:", primes(2))
    # print("prime numbers up to -3:", primes(-3))
