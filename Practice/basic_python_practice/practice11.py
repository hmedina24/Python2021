# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
def main():
    a = map(int,"5,10,15,20,25".split(","))
    b = [a[0],a[-1]]
if __name__ == "__main__":
    main()
