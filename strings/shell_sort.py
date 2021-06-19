#python for sorting an array with the help of shell sorting
def shell_sort(arr):
    gap = len(arr)//2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):

            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1

        while i- gap != -1:
            if arr[i-gap]> arr[i]:
                arr[i-gap],arr[i] = arr[i],arr[i-gap]
            i -= 1
 
        gap //= 2
 
 
# driver to check the code
arr = [12,11,8,4,25,6,87]
print("input array:",arr)
 
shell_sort(arr)
print("sorted array",arr)