def commonPrefix(arr):

    arrlen=len(arr)
    if arrlen==0:
        return -1
    str0=arr[0]
    print(str0)
    ans=0
    str0len=len(str0)


    for i in range(str0len):

        for j in range(arrlen):

            if arr[j][i]==str0[i]:
             
               ans=str0[0:i+1]
               continue
            else:
                if i==0:
                    return -1
                
                return str0[0:i]
            
    return ans

if __name__=="__main__":
    arr=["abcd", "abc", "abref", "abcde"]
    arr2=["QQFV","QQFVvYVwS","QQFVzC"]

    print(commonPrefix(arr2))

