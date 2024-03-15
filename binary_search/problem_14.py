def totalFrequency(arr):

    n=len(arr)

    arr.sort()

    hashArr=[0 for i  in range(arr[n-1]+1)]#[0,0,0,...n]
    print(f"has array initial{hashArr}")


    for j in range(n):

        hashArr[arr[j]]+=1

    print(hashArr)

   

    hashArr.sort()
    totalFrequency=hashArr[len(hashArr)-1]

    for k in range(len(hashArr)-1,0,-1):
        print(hashArr[k])
        if hashArr[k]==hashArr[k-1]:
            totalFrequency+=hashArr[k]
        else:
            break
    return totalFrequency

if __name__=="__main__":

    elements=[1,2,2,3,1,4]
    elements3=[10,12,11,9,6,19,11]
    elements4 = [0,0,0,1,2,1,1]

    print( totalFrequency(elements4))