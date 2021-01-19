

def largestPrimeFactor(num):
    factors = []
    d = 2
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num /= d
        d = d + 1
        if d*d > num:
            if num > 2 : factors.append(num) 
            break
    return factors


def main():
    #factors = largestPrimeFactor(13195) ----> largest prime factor for this number is 29
    factors = largestPrimeFactor(6008514751475143)
    lpf = max(factors) 
    print lpf

if __name__ == "__main__":
    main()
