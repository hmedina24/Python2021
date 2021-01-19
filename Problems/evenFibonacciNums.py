nums = [0,1]

def fibonacci(n):

    if n <= 0:
        print("error: number can't be less than or equal to 0!")
    elif n<=len(nums):
        return nums[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        nums.append(temp_fib)
        return temp_fib
    

def main():
    sumNum = 0
    fibonacci(9)
    for i in nums:
        if i % 2 == 0:
            sumNum += i
    print(sumNum)

if __name__ == "__main__":
    main()
