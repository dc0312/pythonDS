# program that will traverse the binary tree in postOrder left --> right --> root
# Author : DC

class TreeNode:

    def __init__(self,val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def postOrder(self,rootNode):
        if rootNode is None:
            return
        else:
            self.postOrder(rootNode.leftChild)
            self.postOrder(rootNode.rightChild)
            print(rootNode.val)

if __name__ == '__main__':
    node = TreeNode("Drinks")
    node.leftChild = TreeNode("Hot")
    node.rightChild = TreeNode("Cold")
    node.postOrder(node)