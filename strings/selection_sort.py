# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]


for i in range(len(A)):
      
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
              
    # Swap the minimum element 
    A[i], A[min_idx] = A[min_idx], A[i]
  
#test
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]),