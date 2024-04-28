class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def show(self):
        aux = self.head

        while aux != None:
            print(aux.value)
            aux = aux.next


class ManageStack:
    def __init__(self):
        my_stack = Stack()

        my_stack.push(Node(5))
        my_stack.push(Node(10))
        my_stack.push(Node(15))
        my_stack.push(Node(20))

        print("Show stack: ")

        my_stack.show()


ManageStack()
