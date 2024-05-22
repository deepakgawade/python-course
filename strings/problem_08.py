
def getTextInOrder(text):

    textCount=dict()

    for i in text:

        if i not in textCount.keys():
            textCount[i]=text.count(i)

    #sorting
  
    sortlist=   sorted(textCount.items(), reverse=True,key=lambda kv: 
                 (kv[1], kv[0]))
    
    sorteddict=dict(sortlist)


    ans=''
    for i in sorteddict.keys():
        value=sorteddict[i]

        st1=''

        while 0<value:
            st1=st1+i
            value-=1

        ans=ans+st1


    return ans



if __name__=="__main__":

    s='tree'

    getTextInOrder(s)
