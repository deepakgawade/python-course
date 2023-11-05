for i in range(0, 5):
    tointString=""
    strs=""
    for k in range(0,i):
        strs=strs+str(k+1)
    for k in range(0,7-2*i+1):
        strs=strs+" "
    for l in range(0,i):
       
        strs=strs+str(i-l)
    print(strs)