def alternateSignarray(arr):
    n=len(arr)
    k=(n//2)
    positiveIndex=0
    negativeIndex=1
    ansArr=[0 for i in range(n)]
    for i in range(k):
      
        ansArr[positiveIndex] = arr[i]
        positiveIndex+=2

    for j in range(k, n):
        ansArr[negativeIndex]=arr[j]
        negativeIndex+=2

    print(ansArr)

if __name__=="__main__":
    elements=[1,2,-4,-5]
    list2=[1,2,3,-1,-2,-3]

    alternateSignarray(list2)