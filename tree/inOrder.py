# program that will traverse the binary tree in inOrder left --> root --> right
# Author : DC

class TreeNode:

    def __init__(self,val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def inOrder(self,rootNode):
        if rootNode is None:
            return
        else:
            self.inOrder(rootNode.leftChild)
            print(rootNode.val)
            self.inOrder(rootNode.rightChild)

if __name__ == '__main__':
    node = TreeNode("Drinks")
    node.leftChild = TreeNode("Hot")
    node.rightChild = TreeNode("Cold")
    node.inOrder(node)