'''
Implementation of bubble sort
'''

'''
code
'''
def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True

                if swapped == False:
                    break


'''
testing
'''
arr= [7,8,2,69]

bubble_sort(arr)

print("Sorted Array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
