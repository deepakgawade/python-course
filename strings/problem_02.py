def reversed(str):

    temp=''

    n=len(str)
    j=n-1
    i=0
    ans=''


    while i<=j:
      
        
        ans+=str[i]
        if str[i]==" ":
            

            temp=ans+temp
            ans=''

        if i==j:
            temp=ans+" "+temp

        i+=1

    return temp.lstrip().rstrip()





        








if __name__=="__main__":
    s="this is an amazing program"

    print(reversed(s))