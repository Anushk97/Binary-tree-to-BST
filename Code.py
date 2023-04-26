import sys 

class Node:
     
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None
        
 
    @staticmethod
    def storeInorder(root, inorder):     
        if root is None:
            return

        Node.storeInorder(root.left, inorder)
        inorder.append(root.data)
        Node.storeInorder(root.right, inorder)


    @staticmethod
    def countNodes(root):
        if root is None:
            return 0

        return Node.countNodes(root.left) + Node.countNodes(root.right) + 1


    @staticmethod
    def arrayToBST(arr, root):

        if root is None:
            return

        Node.arrayToBST(arr, root.left)

        root.data = arr[0]
        arr.pop(0)

        Node.arrayToBST(arr, root.right)


    @staticmethod
    def binaryTreeToBST(root):
        
        if root is None:
            return

        n = Node.countNodes(root)

        arr = []
        Node.storeInorder(root, arr)
        arr.sort()
        Node.arrayToBST(arr, root)
        


    @staticmethod
    def printPreorder(root, array):
        if root is None:
            return 
        array.append(root.data)
        Node.printPreorder(root.left, array)
        Node.printPreorder(root.right, array)


def to_CBST(input_list):   
    
    node_dict = {}
    for sublist in input_list:
        val, left, right = sublist
        node_dict[val] = Node(val)

    
    for sublist in input_list:
        val, left, right = sublist
        node = node_dict[val]
        if left != 'x':
            node.left = node_dict[left]
        if right != 'x':
            node.right = node_dict[right]

    
    child_nodes = set()
    for sublist in input_list:
        val, left, right = sublist
        if left != 'x':
            child_nodes.add(left)
        if right != 'x':
            child_nodes.add(right)
    for val, node in node_dict.items():
        if val not in child_nodes:
            root = node
            break
    
    Node.binaryTreeToBST(root)
    arr_2 = []
    Node.printPreorder(root,arr_2)
    output = ' '.join([str(elem) for elem in arr_2])
    return output
