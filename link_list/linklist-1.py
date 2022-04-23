#from webob import second


class Node:
 #create a single node
    def  __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    #method to print linkList
    def printList(self):
        temp=self.head
        while(temp):

            print(temp.data)
            temp=temp.next

    

#main code start here

if __name__=='__main__':


    #create empty List
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)

    #link first node with second
    llist.head.next=second
    second.next=third
    third.next=fourth

    llist.printList()