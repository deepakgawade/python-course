def stringCount(s,t):

    if len(s)!=len(t):
        return False
    
    for i in s:

        if s.count(i)!=t.count(i):
            return False
    return True

if __name__=="__main__":
    print(stringCount('CAT','TCT'))