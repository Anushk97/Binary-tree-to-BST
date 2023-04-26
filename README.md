# Binary-tree-to-BST
Algorithm to transform Binary tree to Binary Search Tree

To task is to convert an arbitrary binary tree to a binary search tree with the
same structure and the same set of keys. Let the binary tree be T, the task is to construct a
binary search tree T' such that for a pair of node n and n' at the same position (same path from
the root) in T and T' respectively, the number of nodes in the left subtree of n and the number of
nodes in the left subtree of n' is the same, and the number of nodes in the right subtree of n and
the number of nodes in the right subtree of n' is also the same. In addition, binary tree T' satisfy
the property of binary search trees. 

Test cases will be as follows:
Letter x represents a null node,
so a tree node with two x is a leaf node. The sequence of tree nodes is arbitrary. For example,
‘0:x:x -1:1:-2 -2:0:x 1:x:x’ represents a 4-nodes binary tree rooted at -1, the left child is 1
and the right child is -2, where node 1 is a leaf node. For each binary tree, output the binary
search tree in pre-order traversal separated by space, ‘-1 -2 1 0’

Idea behind this exercise:
1. To learn more about binary trees and how to implement them in code
2. Applications of binary tree include sorting and searching algorithms, indexing databases and more. 
3. If you are looking to practice implementation in python, check out code.py file
