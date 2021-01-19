#find multiple of 3 and 5
def findMultiple(num):
    valSum = 0
    for i in range(0,num):
        if i % 3 == 0 or i % 5 == 0:
            #add i to valSum
            valSum += i
    #print valSum
    print(valSum)

def main():
    findMultiple(1000)

if __name__ == "__main__":
    main()
