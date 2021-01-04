def insertionSort(arr):
    #traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        #move elements of arr[0..i-1], that greater
        #than key, to one position ahead 
        #of their current position
        j = i-1
        while(j >= 0 and key < arr[j]):
            arr[j+1] =  arr[j]
            j-= 1
        arr[j + 1] = key

    for i in range(len(arr)):
        print("%d" %arr[i])


def main():
    #lets create an array
    nums = [9,3,6,2,7,1,5,4]
    
    insertionSort(nums)
   
    


if __name__ == "__main__":
    main()

 
