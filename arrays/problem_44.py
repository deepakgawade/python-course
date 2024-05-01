def numberBrackets(s):

    n=len(s)
    count=0
    maxcount=0

    for i in range(n):

        if s[i]=='(':
            count+=1
        elif s[i]==")":
            maxcount=max(maxcount,count)
            count-=1
        else: 
            continue

    return maxcount

if __name__=="__main__":
    text='(3*(4*(5*(6))))'
    text2='((0-9))(1-3)(((4+5)((0/2)(5-1)(5/9))(9-0)((4/3)(2+7))(3-6)(((6+2)))))'

    print(f"Number of () are {numberBrackets(text2)}")



