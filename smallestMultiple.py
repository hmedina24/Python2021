def main():
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in range(2520, 100000):
        for j in nums:
            if i / j == 0:
                smallestMultiple = i
    print(smallestMultiple)

if __name__ == "__main__":
    main()
