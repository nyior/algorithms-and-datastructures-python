from typing import Any

class Node:
    """
         models a node in a doubly linked list
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    """
        models a doubly linked list data structure
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.number_of_nodes = 0

    #0(1) operation
    def insert_end(self, data: Any) -> None:
        new_node = Node(data)
        self.number_of_nodes += 1

        # if linked list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # there is at least one item
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail

            self.tail = new_node


    # 0(n) operation. Remember, doubly linked lists could be traversed
    # in both directions.
    def traverse_forward(self) -> None:
        place_holder_node = self.head

        while place_holder_node is not None:
            print(place_holder_node.data)
            place_holder_node = place_holder_node.next_node

    # O(n) operation
    def traverse_backward(self) -> None:
        place_holder_node = self.tail

        while place_holder_node is not None:
            print(place_holder_node.data)
            place_holder_node = place_holder_node.previous_node


if __name__ == "__main__":
    doubly_list = DoublyLinkedList()

    doubly_list.insert_end(1)
    doubly_list.insert_end(2)
    doubly_list.insert_end(3)

    doubly_list.traverse_forward()
    print("______________________________")
    doubly_list.traverse_backward()
