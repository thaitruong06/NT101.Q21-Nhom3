import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # viết n-1 = d * 2^s
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def random_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= 1
        if is_prime(num):
            return num


def largest_primes_below_mersenne():
    M = 2**89 - 1
    count = 0
    n = M - 1

    primes = []

    while count < 10 and n > 1:
        if is_prime(n):
            primes.append(n)
            count += 1
        n -= 1

    return primes


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


def main():

    print("=== PRIME GENERATION ===")
    print("Prime 8-bit :", random_prime(8))
    print("Prime 16-bit:", random_prime(16))
    print("Prime 64-bit:", random_prime(64))

    print("\n=== PRIME CHECK ===")
    num = int(input("Enter number to check prime: "))
    if is_prime(num):
        print(num, "is PRIME")
    else:
        print(num, "is NOT prime")

    print("\n=== LARGEST PRIMES BELOW MERSENNE ===")
    primes = largest_primes_below_mersenne()
    for i, prime in enumerate(primes, 1):
        print(f"{i}. {prime}")

    print("\n=== GCD CALCULATION ===")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("GCD(", a, ",", b, ") =", gcd(a, b))

    print("\n=== MODULAR EXPONENTIATION ===")
    base = int(input("Enter base a: "))
    exp = int(input("Enter exponent x: "))
    mod = int(input("Enter modulus p: "))

    result = mod_exp(base, exp, mod)

    print(base, "^", exp, "mod", mod, "=", result)


if __name__ == "__main__":
    main()
