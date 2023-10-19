class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=node(data)
            new.next=self.tail.next
            self.head.prev=new
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        print(self.head.val,end="->")
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8]
c=dll()
for i in l:
    c.insertatend(i)
c.printing()
        




    
