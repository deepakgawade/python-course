def fibonaci(N):

    if N<=1:
        return N
    last =fibonaci(N-1)
    slast=fibonaci(N-2)

    return  last+ slast
    

if __name__=="__main__":
    print(fibonaci(5))