for i in range(4):
    strs=""
    for j in range(3-i):
        strs=strs+" "
    ch=64
    breakpoint = (2*i+1)/2
    for k in range(2*i+1):
       
        if(k<breakpoint):
            ch=ch+1
            strs=strs+chr(ch) 
        else:
            ch=ch-1
            strs=strs+chr(ch) 
    for j in range(3-i):
        strs=strs+" "
    print(strs)
