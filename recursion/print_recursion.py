
def printnumber(n):
    print(n)
    if n==0: 
        return
    n-=1
    printnumber(n)
def printName(n):
    print("Tejasvini")
    if n==0: 
        return
    n-=1
    printName(n)




def print3(count):
    if count==5:
        return
    print(count)
    count+=1
    print3(count)

if __name__=="__main__":
    count=0
    print3(count)
    printName(5)
    printnumber(10)