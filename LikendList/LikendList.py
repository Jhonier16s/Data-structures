class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.nq = 0

    def addStart(self, node):
        if self.head == None:
            self.head = node
            self.last = node
        else:
            node.next = self.head
            self.head = node
        self.nq += 1

    def addEnd(self, node):
        if self.head == None:
            self.last = node
            self.head = node
        else:
            self.last.next = node
            self.last = node
        self.nq += 1

    def addBetween(self, node, p):
        if self.head == None or p == 0:
            self.addStart(node)
        elif p > self.nq:
            self.addEnd(node)
        else:
            aux = self.head
            for i in range(p):
                aux = aux.next

            node.next = aux.next
            aux.next = node
        self.nq += 1

    def removeStart(self):
        if self.head != None:
            self.head = self.head.next
            self.nq -= 1

    def removeEnd(self):
        if self.head != None:
            aux = self.head
            prev = None
            while aux.next != None:
                prev = aux
                aux = aux.next
            prev.next = None
            self.nq -= 1

    def removeBetween(self, p):
        if self.head != None:
            if p <= 0:
                self.removeStart()
            elif p > self.nq:
                self.removeEnd()
            else:
                aux = self.head
                prev = None
                for i in range(p):
                    prev = aux
                    aux = aux.next
                prev.next = aux.next
            self.nq -= 1

    def updateNode(self, p, nv):
        if self.head != None:
            if p >= self.nq:
                self.last.value = nv
            else:
                aux = self.head
                for i in range(p):
                    aux = aux.next
                aux.value = nv

    def findNodePosition(self, value):
        if self.head != None:
            aux = self.head
            count = 0
            while aux != None:
                if aux.value == value:
                    print("The position of node is: ", count)
                    return
                aux = aux.next
                count += 1
            print("Not find the node")

    def show(self):
        aux = self.head

        while aux != None:
            print(aux.value)
            aux = aux.next

    def showReverse(self):
        self.showReverseAuxiliar(self.head)

    def showReverseAuxiliar(self, node):
        if node == None:
            return

        self.showReverseAuxiliar(node.next)
        print(node.value)


class ManageLinkedList:
    def __init__(self):

        my_linkedList = LinkedList()
        print("AddStart: ")
        my_linkedList.addStart(Node(1))
        my_linkedList.addStart(Node(2))
        my_linkedList.addStart(Node(3))
        print("AddEnd: ")
        my_linkedList.addEnd(Node(4))
        my_linkedList.addEnd(Node(5))
        my_linkedList.addEnd(Node(6))

        print("AddBetween: ")

        my_linkedList.addBetween(Node(100), 2)
        my_linkedList.addBetween(Node(200), 100)
        my_linkedList.addBetween(Node(300), 0)

        print("Show List: ")

        my_linkedList.show()
        print("remove start and  remove End: ")
        """ my_linkedList.removeStart()
        my_linkedList.removeEnd() """
        my_linkedList.removeBetween(4)
        print("Show List: ")

        my_linkedList.updateNode(10000, 120)
        my_linkedList.findNodePosition(120)

        my_linkedList.show()


ManageLinkedList()
