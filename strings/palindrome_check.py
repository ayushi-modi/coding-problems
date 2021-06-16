'''
Check whether string is palindrome or not
   1. Understand problem
   2. Know inputs and output

   "abba"
   "neveroddoreven"
'''


'''
Code
'''
def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


'''
Testing
'''

output = is_palindrome("laptop")
print("---------------------")
print(output)

'''
Measure complexity
    1. Time Complexity
    2. Space Complexity
'''
# Time Complexity O(n)
# Space Complexity O(1)
