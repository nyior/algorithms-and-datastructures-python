from typing import Any

class Node:
    """
         models a node in a BST
    """

    def __init__(self, data: Any, parent: Any) -> None:
        self.parent = parent
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root_node = None

    def search(self, data: Any) -> Node:
        if self.root_node:
            self._binary_search(data, self.root_node)

    def _binary_search(self, data: Any, node: Node) -> Node:
        if not node:
            return

        if data < node.data:
            self._binary_search(data, node.left_child)
        elif data > node.data:
            self._binary_search(data, node.right_child)
        else: return node

    def insert(self, data: Any) -> None:
        if not self.root_node:
            self.root_node = Node(data, None)
        else:
            self._insert_node(data, self.root_node)

    def _insert_node(self, data: Any, node: Node) -> None:
        if data < node.data:
            if node.left_child:
                self._insert_node(data, node.left_child) # recursively call until it
                                            # finds the left-most leaf node
            else: 
                node.left_child = Node(data, node)
        else:

            if node.right_child:
                self._insert_node(data, node.right_child) # recursively call until it
                                            # finds the right-most leaf node
            else: 
                node.right_child = Node(data, node)

    def remove(self, data: Any) -> None:
        node = self.search(data)

        if node:
            if not node.left_child and not node.right_child: # removing leaf node
                node.parent.left_child = None if node == node.parent.left_child \
                    else  node.parent.right_child = None

            # if node.left_child and node.right_child: # removing node with left and right child
            #     node.parent.left_child = None if node.data < node.parent.data \
            #         else  node.parent.right_child = None

            if node.left_child: # removing node with left child only
                node.parent.left_child = node.left_child if node == node.parent.left_child \
                    else  node.parent.right_child = node.left_child

            if node.right_child: # removing node with right child only
                node.parent.left_child = node.right_child if node == node.parent.left_child \
                    else  node.parent.right_child = node.right_child


    def traverse(self) -> None:
        if self.root_node:
            self._traverse_in_order(self.root_node)

    # Left node - root node - right node
    def _traverse_in_order(self, node: Node):
        if node.left_child:
            """
                under the hood the items would be placed
                on the call stack, and when the leftmost
                leaf node is reached the items are then popped
                out one after the other
            """
            self._traverse_in_order(node.left_child) 

        print(node.data) # print root node

        if node.right_child:
            self._traverse_in_order(node.right_child)

    def max_value(self) -> None:
        if self.root_node:
            self._get_max_value(self.root_node)

    def _get_max_value(self, node: Node):
        if node.right_child:
            return self._get_max_value(node.right_child)
        
        return node.data

    def min_value(self) -> None:
        if self.root_node:
            self._get_min_value(self.root_node)

    def _get_min_value(self, node: Node):
        if node.left_child:
            return self._get_min_value(node.left_child)
        
        return node.data
        

