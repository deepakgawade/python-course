def mooreAlgo(arr):
    n=len(arr)
    count=0
    element=None

    for i in range(n):

        if count==0:
            count=1
            element=arr[i]

        elif element==arr[i]:
            count+=1
        else:
            count-=1
    count=0
    for i in range(n):
        if arr[i]==element:
            count+=1

    if count>(n/2):
        return element
    return -1
    