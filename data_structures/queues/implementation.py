from typing import Any
from linked_lists.doubly_linked_list.implementation import DoublyLinkedList

class Queue:

    def __init__(self) -> None:
        self.queue = []

    def is_empty(self) -> bool:
       return self.queue == []

    # O(1) running time
    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    # O(n) running time --after deleting the first element
    # a hole would be left in the DS -- we'd then have to shift the
    # elements to fill up the hole.
    def dequeue(self) -> Any:
        if self.queue.is_empty():
            return

        data = self.queue[0]
        del self.queue[0]

        return data
    
    # O(1) running time
    def peek(self) -> Any:
        return self.queue[-1]


# ---------QUEUE WITH LINKED LIST-------------
# It is more appropriate that we implement queues with linkedlist
# -- that would cut down the running time of the dequeue op to O(1)
# however, if we choose to go with singly-linked-list, the enqueue op
# would have an O(n) running time(since we'd have to find the last item)
# The doubly linked list is more suitable for this purpose

class Queue:

    def __init__(self) -> None:
        self.queue = DoublyLinkedList()

    def is_empty(self) -> bool:
       return self.queue.head == None

    def enqueue(self, data: Any) -> None:
        self.queue.insert_end(data)

    def dequeue(self) -> Any:
        if self.queue.is_empty():
            return

        data = self.queue.head.data

        # make the node next to the head node, the head node
        next_node = self.queue.head.next_node

        next_node.previous_node = None # detach next node from head
        self.queue.head.next_node = None # detach head from next node
        self.queue.head = next_node # make next_node the head node

        return data

    # O(1) running time
    def peek(self) -> Any:
        return self.queue[-1]