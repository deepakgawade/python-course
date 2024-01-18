

def linearSearch(arr, num):

    n=len(arr)

    for i in range(n):
        if arr[i]==num:
            return True
    return False


def longestConsecutive(arr):
    n= len(arr)
    longest=1
    

    # run first loop to take one number

    for i in range(n):
        x=arr[i]
        count=1
        #check for each number its consecutive numbers throughout array
        while linearSearch(arr, x+1):
            x=x+1
            count+=1 #and run again for each number in array


        longest=max(longest, count)#check 
    
    return longest


def betterLongestConsecutive(arr):

    n = len(arr)
    arr.sort()
    longest=1
    count=0
    lastSmaller=float('-inf')

    for i in range(n):

        if arr[i]-1==lastSmaller: #check current and prevoius element 
            count+=1
            lastSmaller=arr[i]
        elif arr[i] != lastSmaller:# if not equal then set new count and set new lastsmaller
            count=1
            lastSmaller=arr[i]
        
        longest= max(count, longest) #here it checks for longest one
    return longest

def optimalSetLongestConsecutive(arr):
    n = len(arr)
    if n==0:
        return 0

    longest=1
    count=0

    s=set()

    for i in range(n):
        s.add(arr[i])
    
    for it in s:
        if it-1 not in s:
            count+=1
            x=it
            while x+1 in s:
                count+=1
                x+=1
            longest=max(longest,count)
    return longest




if __name__=="__main__":
    a=[100, 200, 1, 2, 3, 4]
    b=[3, 8, 5, 7, 6, 9]
    ans= longestConsecutive(b)
    ans2= betterLongestConsecutive(b)
    print(ans)
    print(ans2)


