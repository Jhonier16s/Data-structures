class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.last = None

    def push(self, node):
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def show(self):
        aux = self.head

        while aux != None:
            print(aux.value)
            aux = aux.next

    def pop(self):
        if self.head != None:
            self.head = self.head.next


class ManageQueue:
    def __init__(self):
        my_queue = Queue()

        my_queue.push(Node(5))
        my_queue.push(Node(10))
        my_queue.push(Node(15))
        my_queue.push(Node(20))

        print("Show Queue: ")

        my_queue.show()

        print("POP Queue ")

        my_queue.pop()

        print("Show Queue: ")

        my_queue.show()


ManageQueue()
