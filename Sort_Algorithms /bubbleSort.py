def bubbleSort(arr):
    n = len(arr)

    #traverse through all array elements
    for i in range(n):
        #last i element are already in place 
        for j in range(0, n-i-1):
            #traverse the array from 0 to n-i-1
            #swap if the element found is greater
            #than the next element 
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array is: ")
    for k in range(len(arr)):
        print("%d" %arr[k])

def main():
    nums = [9,3,6,2,7,1,5,4]
    #Bubble Sort function 
    bubbleSort(nums)

if __name__ == "__main__":
    main()
