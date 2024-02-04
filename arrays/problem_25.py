def nCr(n,r):

    res = 1

    for i in range(r):

        res=res*(n-i)

        res=res/(i+1)
    
    return res
##time complexity O(r)


def optimizeVar2(n):
    ans = 1
    row=[1]

    for i in range(1,n):
        ans = ans *(n-i)
        ans = ans // i
        row.append(ans)

    return row
    
#O(N)
        
def optimizeVar3(n):
    ans=[]
    for i in range(1,n+1):
        row=optimizeVar2(i)
        ans.append(row)
    return ans

if __name__=="__main__":

    ans=optimizeVar3(4)
     

    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()



    pass