
def printPattern(N):


    for i in range(N):
        strs=""

        for j in range(N-i):
            strs=strs+"*"
        for k in range(2*i):
            strs=strs+" "

        for l in range(N-i):
            strs=strs+"*"
        print(strs)
    for i in range(N+1):
        strs=""

        for j in range(i):
            strs=strs+"*"
        for k in range(2*N-2*i):
            strs=strs+" "

        for l in range(i):
            strs=strs+"*"
        print(strs)

if __name__=="__main__":
        printPattern(8)
    


        