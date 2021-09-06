def fact(n):                                                #function for calculating factorial with only parameter n(from user)

        res = 1

        for i in range(2,n+1):                          #loop for necessary calculations

             res = res * i

        return res                                            #function returning a value





n = int(input())                                             #for taking input from user and storing in "n"

print(fact(n))                                                #for the final output