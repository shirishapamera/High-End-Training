#depth first search has traversals
#1.inorder,2.preorder,3.postorder
class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    printing(root.left)
    print(root.val)
    printing(root.right)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(4)
printing(root)
