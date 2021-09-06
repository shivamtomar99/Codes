def maxmin(arr):                           # A function to find largest and smallest value which takes array as an input

    ans1 = min(arr)                         # Smallest value stored in ans1

    ans2 = max(arr)                       #largest stored in ans2



    return ans2 , ans1                      #function will return largest and smallest value







arr = list(map(int,input().split()))

print(maxmin(arr))