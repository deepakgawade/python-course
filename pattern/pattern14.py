for i in range(4):
    strs=""
    for j in range(4):
        if(i==0 or j==0 or i==4-1 or j==4-1):

            strs=strs+"*"
        else:
            strs=strs+" "
    print(strs)
    