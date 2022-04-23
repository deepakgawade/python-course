class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    #created head of list
    def __init__(self,head=None):
        self.head=head
    
    #functioin to add node at beginning
    def push(self,new_data):
        
        #initialize a node    
        new_node=Node(new_data)

        #point previous head to next of new node
        new_node.next=self.head

        #create new head

        self.head=new_node
    
    #add node after a given node
    def insertAfter(self,prevNode,new_data):

        #check if prevNode is none
        if prevNode is None:
            print("the previuos node must be in linklist")
            return
        
        #initialize with node with new data
        new_node=Node(new_data)

        #point previous next new_node next
        new_node.next=prevNode.next

        #point new previous next to new node
        prevNode.next=new_node

    #append  new node at end of list
    def append(self,data):
    
        #create ne node with data
        new_node=Node(data)

        #check if list is empty
        if self.head is None:
            self.head=new_node
            return
        #traverse till it reaches end of list
        temp=self.head
        while(temp.next):
            temp=temp.next
        #at end bind new node
        temp.next=new_node
     #printing function list   
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    
    llist=LinkedList()
    
    llist.append(7)
    llist.push(1)
    llist.append(3)

    llist.push(6)

    llist.printList()

    llist.insertAfter(llist.head.next,10)

    llist.printList()



