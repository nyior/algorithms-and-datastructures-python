from linked_lists.singly_linked_list.implementation import LinkedList, Node
from stacks.implementation import Stack



"""
# problem 1

Suppose we have a standard linked list. 
Construct an in-place (without extra memory) algorithm 
thats able to find the middle node!
"""

# 0(n) running time.
def get_middle_node(linked_list: LinkedList) -> Node:
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head

    while fast_pointer.next_node and fast_pointer.next_node.next_node:
        fast_pointer = fast_pointer.next_node.next_node
        slow_pointer = slow_pointer.next_node
    return slow_pointer.data


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_beginning(1)
    linked_list.insert_beginning(2)
    linked_list.insert_beginning(3)

    print(get_middle_node(linked_list))


""" 
    # problem 2

    Construct an in-place algorithm to reverse a linked list!
"""

def reverse_linked_list(linked_list: LinkedList) -> Node:
    next_node = None
    previous_node = None
    current_node = linked_list.head
    
    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node 

    linked_list.head = previous_node
            