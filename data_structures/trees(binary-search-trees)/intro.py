"""
    the major drawback with manipulating items at arbitrary locations
    e.g searching, inserting, deleting etc in linkedlists and arrays
    is that it has an O(n) running time complexity. Binary search trees
    exist to solve this problem.

    Items in a BST are usually stored based on nodes(starting with the root node)
    and usually in a sorted order. This is just so the binary search approach could
    be leveraged to lookup items in the BST with an OLogN running time. 
    The OlogN running time is comparatively more efficient than O(n)

    Each node in a binary could have a maximum of two child nodes(left and right nodes).
    The value of the left node must always be smaller than that of its parent node while
    that of the right node must always be bigger than that of its parent. Essentially, all the
    values on the left side of a node must be smaller than the value at the node, and all the values
    on the right side of the node must be greater than the value at the node.

    A BST is balanced if the number of nodes on the left subtree roughly equals the number
    of nodes on the right subtree
"""