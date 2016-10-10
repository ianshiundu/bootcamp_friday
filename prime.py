def primes_method(n):
    out = list()
    for num in range(1, n+1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return out
primes_method()