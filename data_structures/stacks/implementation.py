from typing import Any

class Stack:

    def __init__(self) -> None:
        self.stack = []

    def stack_size(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
       return self.stack == []

    # O(1) running time
    def push(self, data: Any) -> None:
        self.stack.append(data)

    # O(1) running time
    def pop(self) -> Any:
        if self.stack.is_empty():
            return

        data = self.stack[-1]
        del self.stack[-1]

        return data

    # O(1) running time
    def peek(self) -> Any:
        return self.stack[-1]


# There is no point implementing a stack with a linkedlist 
# since we'd majorly be interacting with the topmost item
# in the stakc -- this is what arrays are optimized for