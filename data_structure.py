class Node:
    def __init__(self, data, left=None, right=None):
        self.left=left
        self.right=right
        self.data=data

def callback(value):
    print(value, end=' ')

def preorder(node, callback):
    if(node != None):
        callback(node.data)
        preorder(node.left, callback)
        preorder(node.right, callback)

def inorder(node, callback):
    if(node != None):
        inorder(node.left, callback)
        callback(node.data)
        inorder(node.right, callback)

def postorder(node, callback):
    if(node != None):
        postorder(node.left, callback)
        postorder(node.right, callback)
        callback(node.data)
