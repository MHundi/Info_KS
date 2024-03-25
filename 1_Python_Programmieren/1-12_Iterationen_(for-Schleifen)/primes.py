def is_prime(x: int, ps: list[int]) -> bool:
    if x <= 1:
        return False
    for p in ps:
        if x % p == 0:
            return False
    return True


def primes(n: int) -> list[int]:
    ps = []
    for i in range(2, n + 1):
        if is_prime(i, ps):
            ps = ps + [i]
    return ps
    


def main():
    erg = []
    a=input("Insert the upper ")
    a = int(a)
    erg = primes(a)
    print(erg)
    

if __name__ == "__main__":
    main()
    #assert primes(1) == []
    #assert primes(3) == [2, 3]
    #assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]