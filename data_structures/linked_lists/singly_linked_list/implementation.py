from typing import Any

class Node:
    """
        models a node in a linked list
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next_node = None


class LinkedList:
    """
        models a linked list data structure
    """

    def __init__(self) -> None:
        self.head = None
        self.number_of_nodes = 0

    # 0(1) operation
    def insert_beginning(self, data: Any) -> None:
        new_node = Node(data)
        self.number_of_nodes += 1

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(n) operation
    def insert_end(self, data: Any) -> None:
        new_node = Node(data)
        self.number_of_nodes += 1

        place_holder_node = self.head

        while place_holder_node.next_node is not None:
            place_holder_node = place_holder_node.next_node

        place_holder_node.next_node = new_node

    def size(self) -> int:
        return self.number_of_nodes

    # 0(n) operation
    def traverse(self) -> None:
        place_holder_node = self.head

        while place_holder_node is not None:
            print(place_holder_node.data)
            place_holder_node = place_holder_node.next_node

    # O(n) operation
    def remove_item(self, data: Any) -> None:

        if self.head is None:
            return

        place_holder_node = self.head
        previous_node = None

        while place_holder_node is not None \
            and place_holder_node.data != data:

            previous_node = place_holder_node
            place_holder_node = place_holder_node.next_node

        if place_holder_node is None:
            return

        self.number_of_nodes -= 1

        # if at the end of the loop previous node is None and 
        # placeholder node is not, it means it's the head we are to get rid of
        if previous_node is None:
            self.head = place_holder_node.next_node
        else:
            previous_node.next_node = place_holder_node.next_node

        


