def twoNumExist(arr,k):

    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            
            sum=arr[i]+arr[j]

            if sum==k:
                return "Yes"

    return "No"

def twoNumExistIndex6(arr,k):

    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            
            sum=arr[i]+arr[j]

            if sum==k:
                return [i,j]

    return [-1,-1]



#using dict key value pair
def withDict(arr,k):
    n=len(arr)
    newDict={}
    for i in range(n):
        moreNeeded= k-arr[i]
        if moreNeeded in newDict:
            return "Yes"
        newDict[arr[i]]=i

    return "No"

if __name__=="__main__":
    elements=[2,6,5,8,11]
    # print(twoNumExist(elements,15))
    # print(twoNumExistIndex6(elements,15))
    print(withDict(elements,14))
    

