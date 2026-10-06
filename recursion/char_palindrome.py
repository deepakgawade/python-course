def palidrome(i,longstring):
    if i>=len(longstring)/2:
        return True
    if longstring[i]!=longstring[len(longstring)-1-i]:
        return False
    
    return palidrome(i+1,longstring)

    
if __name__=="__main__":
   daat="malayalam"
   print(daat)
   value= palidrome(0,daat)
   print(value)
