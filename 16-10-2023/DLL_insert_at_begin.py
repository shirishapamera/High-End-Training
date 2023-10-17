class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.head.prev=new
            new.next=self.head
            self.head=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8]
c=dll()
for i in l:
    c.insertatbegin(i)
c.printing()
        