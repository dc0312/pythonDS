# program that will traverse the binary tree in preorder root --> left --> right
# Author : DC

class TreeNode:

    def __init__(self,val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def preOrder(self,rootNode):
        if rootNode is None:
            return
        print(rootNode.val)
        self.preOrder(rootNode.leftChild)
        self.preOrder(rootNode.rightChild)

if __name__ == '__main__':
    node = TreeNode("Drinks")
    node.leftChild = TreeNode("Hot")
    node.rightChild = TreeNode("Cold")

    node.preOrder(node)
