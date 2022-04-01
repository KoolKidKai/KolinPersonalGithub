def findprimes(min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
    print()


def primes():
    minimum = int(input(" Enter the Minimum Value for Primes: "))
    maximum = int(input(" Enter the Maximum Value for Primes: "))
    findprimes(minimum, maximum)

def primesTester():
    minimum = 45
    maximum = 76
    print("minimum = 45 | maximum = 76 | primes: ", end="")
    findprimes(minimum, maximum)
    print()
    minimum = 5
    maximum = 37
    print("minimum = 5 | maximum = 37 | primes: ", end="")
    findprimes(minimum, maximum)
    print()
    minimum = 65
    maximum = 172
    print("minimum = 65 | maximum = 172 | primes: ", end="")
    findprimes(minimum, maximum)

if __name__ == "__main__":
    primes()
    primesTester()