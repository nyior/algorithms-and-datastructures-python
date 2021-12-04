"""
    PROBLEM 1 --
    The aim is to design an algorithm that can return the 
    maximum item of a stack in O(1) running time complexity. 
    We can use O(N) extra memory!

    --- to solve this, we will just introduce a varibale
    that keeps track of the items inserted into the stack
"""
from stacks.implementation import Stack

from typing import Any


class MaxStack(Stack):

    def __init__(self) -> None:
        super().__init__()
        self.max_item = None

    def push(self, data: Any) -> None:
        super().push(data)

        if super().is_empty():
            self.max_item = data
        else:
            if data > self.max_item:
                self.max_item = data

    def get_max_item(self):
        return self.max_item


"""
    PROBLEM 2 --
    Implement a queue with a stack!
"""


class QueueFromStack:

    def __init__(self) -> None:
        self.queue = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, data: Any) -> None:
        self.queue.push(data)

    def dequeue(self) -> Any: # recursively
        if self.queue.stack_size == 1: # base case
            return self.queue.pop()
        else:
            item = self.queue.pop # remove the topmost item
            
            dequeued_item = self.dequeue() # this removes the topmost item repeatedly 
                                            # until the base case is reached
            self.queue.push(item) # reinsert all the items placed on the call-stack once the
                                    # base case is reached
            return dequeued_item

    def peek(self) -> Any:
        self.queue.peek()