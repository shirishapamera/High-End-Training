class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new
    def deleteatend(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=sll()
for i in l:
    c.insertatbegin(i)
     
print("Deleted Element:",c.deleteatend())
print("After Deleting at end the list is:")
c.printing()