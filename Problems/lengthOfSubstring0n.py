# Python3 program to find the length of the longest substring 
# without repeating characters 
NO_OF_CHARS = 256
  
def longestUniqueSubsttr(string): 
  
    # Initialize the last index array as -1, -1 is used to store 
    # last index of every character 
    lastIndex = [-1] * NO_OF_CHARS 
  
    n = len(string) 
    res = 0   # Result 
    i = 0
  
    for j in range(0, n): 
        # Find the last index of str[j] 
        # Update i (starting index of current window) 
        # as maximum of current value of i and last 
        # index plus 1 
        i = max(i, lastIndex[ord(string[j])] + 1); 
  
        # Update result if we get a larger window 
        res =  max(res, j - i + 1) 
  
        # Update last index of j. 
        lastIndex[ord(string[j])] = j; 
  
    return res 
  
# Driver program to test the above function 
string = "geeksforgeeks"
print ("The input string is " + string) 
length = longestUniqueSubsttr(string) 
print ("The length of the longest non-repeating character" +
       " substring is " + str(length))
