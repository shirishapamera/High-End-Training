'''#basics of linked list
class Node:
    def _init_(self,val=0):
        self.val=val
        self.next=None
o1=Node(1)
o2=Node(2)
o3=Node(3)
o1.next=o2
o2.next=o3
print(o1,o1.val,o1.next)
print(o1,o2.val,o2.next)
print(o1,o3.val,o3.next)
#print(o1,o2,o3,sep='\n')'''
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o1.next=node(2)
o1.next.next=node(3)
print(o1.val,o1.next.val,o1.next.next.val)