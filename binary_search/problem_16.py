def nthRoot(nRoot,number):
    tempList=[x for x in range(1,number+1)]

    n=len(tempList)

    low=0
    high=n-1

    while low<=high:

        mid = (low+high)//2

        product=mid**nRoot

        if product==number:

            return mid
        
        elif product<number:
            low=mid+1

        else: 
            high=mid-1
    return -1


if __name__=="__main__":

    nthroot=3
    value=64

    print(nthRoot(nthroot,value))
