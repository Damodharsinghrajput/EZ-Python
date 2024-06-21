class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.value=data
def topveiw(root):
    temp=node(root,0)
    Q=[temp]
    Q.append(None)