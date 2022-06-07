


class BinarySearch :
    def locate_card(self, cardList, query):
        lo,hi=0,len(cardList)-1
        print(hi)

        while lo<=hi:
            mid=(lo+hi) // 2

            midNum=cardList[mid]

            if midNum==query:
                return  mid
            elif midNum<query:
                hi=mid-1


            elif midNum>query:
                lo=mid+1
        return -1    


if __name__=='__main__':
    test=[]
    test0={"list":[9,8,7,6,5,4,3,2],
    "query":5,"output":4}
    test.append(test0)

    search=BinarySearch()

    num=search.locate_card(cardList=test0["list"],query=test0["query"])

    if num==test0["output"]:
        print("Found")
        print(num)
    else:
        print("Not found")