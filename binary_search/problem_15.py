def squareRootOfNum(arr,X):
    n=len(arr)

    low= 0
    high=n-1

    while low<=high:

        mid = (low+high)//2
        square=mid*mid

        if square==X:

            return mid
        elif square<X:
            low=mid+1
        else:
            high=mid-1

if __name__=="__main__":
    sqr=4

    elements=[x for x in range(1,sqr+1)]

    print(squareRootOfNum(elements,sqr))