"""
    In the linked list data structure, items are stored as nodes. 
    Each node in a doubly linked list contains data, and the references
    to the next and previous nodes in the linked list.

    Unlike arrays, linked lists are dynamic data structures(no resize
    operation is required). In addition to, manipulating the first item with an O(1)
    run timecomplexity as in singly linked lists, doubly linked lists also make manipulating
    the last item so much easier. It comes with an 0(1) runtime complexity.

    However, doubly linked lists don't do  so well when it comes to manipulating
    items at arbitrary locations. Further, doubly linked lists could be traversed in both
    directions. All the mentioned ops in this paragraphs have an O(n) runtime complexity.

"""