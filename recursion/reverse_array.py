def reverseArray(arrx,n,i,arry):
   arry.append( arrx[n-i])

   if n-i==0:
      
      print(arry)
      return
   i+=1
   reverseArray(arrx,n,i,arry)


if __name__=="__main__":
   x=[1,2,3,4,5]
   reverseArray(x, len(x)-1,0, [])

    
