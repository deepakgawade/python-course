def brutemergeSortedArray(arrA,arrB):

    n1=len(arrA)
    n2=len(arrB)
    answerTemp=[0]*(n1+n2)
    left=0
    right=0
    index=0
    while left<n1 and right<n2:

        if arrA[left]<arrB[right]:
            answerTemp[index]=arrA[left]
            index+=1
            left+=1
        else:
            answerTemp[index]=arrB[right]
            index+=1
            right+=1
    while left< n1:
        answerTemp[index]=arrA[left]
        index+=1
        left+=1
    while right< n2:
        answerTemp[index]=arrA[right]
        index+=1
        right+=1
        
    for i in range(n1+n2):
        if i<n1:
            arrA[i]=answerTemp[i]
        else:
            arrB[i-n1]=answerTemp[i]
    print(arrA)
    print(arrB)
    #TC O(n+m) +O(n+m)
    #SC O(n+m)


def optimalAppaoch1(arrA,arrB):

    n1=len(arrA)
    n2=len(arrB)

    left= n1-1
    right=0

    while left>=0 and right<n2:

        if arrA[left]>arrB[right]:
            temp=arrA[left]
            arrA[left]=arrB[right]
            arrB[right]=temp
            left-=1
            right+=1 

        else: break

        
    arrA.sort()
    arrB.sort()

    print(arrA)
    print(arrB)

    #TC O(min(n,m)) + O(nlogn)+ O(mlogm)
    #SC O(1)

def swapIfGreater(arrA, arrB, ind1, ind2):
    if arrA[ind1] > arrB[ind2]:
        arrA[ind1], arrB[ind2] = arrB[ind2], arrA[ind1]

def optimal2(arrA, arrB):

    n1=len(arrA)
    n2=len(arrB)

    tlen= n1+n2

    gap=(tlen//2)+(tlen%2)

    while gap>0 :
        left=0
        right=left+gap

        while right<tlen:
            #arrA and arrB
            if left<n1 and right>=n1:
                swapIfGreater(arrA, arrB, left, right - n1)




                #arrB sand arrB
            elif left>=n1:
                swapIfGreater(arrB, arrB, left - n1, right - n1)


            else:
                swapIfGreater(arrA, arrA, left, right)
            left+=1
            right+=1


        if gap == 1:
            break
        # Otherwise, calculate new gap:
        gap = (gap // 2) + (gap % 2)

    print(arrA)
    print(arrB)






    



if __name__=="__main__":


    arr1 = [1, 4 ,8 ,10]
    arr2=[2, 3, 9]

    optimal2(arr1,arr2)





