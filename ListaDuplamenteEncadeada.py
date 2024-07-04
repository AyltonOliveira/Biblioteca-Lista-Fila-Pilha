class ListNode:
    def __init__(self, data, nextNode=None, antNode=None):
        self.data = data
        self.nextNode = nextNode
        self.antNode = antNode

class DoublyLinkedListIterator:
    def __init__(self, nextNode=None):
        self.firstNode = nextNode
        self.lastNode = nextNode
        self.iterator = nextNode
        if nextNode:
            self.size = 1
        else:
            self.size = 0

    def get_iterator(self):
        return self.iterator

    def addNode(self, data):
        newNode = ListNode(data, None)
        if self.size == 0:
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.lastNode:
            self.lastNode.nextNode = newNode
            newNode.antNode = self.lastNode
            self.lastNode = newNode
            self.iterator = newNode
        else:
            newNode.nextNode = self.iterator.nextNode
            newNode.antNode = self.iterator
            self.iterator.nextNode.antNode = newNode
            self.iterator.nextNode = newNode
            self.iterator = newNode
        self.size += 1
        return True

    def insNode(self, data):
        newNode = ListNode(data, None)
        if self.size == 0:
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.firstNode:
            newNode.nextNode = self.firstNode
            self.firstNode.antNode = newNode
            self.firstNode = newNode
            self.iterator = newNode
        else:
            newNode.nextNode = self.iterator
            newNode.antNode = self.iterator.antNode
            self.iterator.antNode.nextNode = newNode
            self.iterator.antNode = newNode
            self.iterator = newNode
        self.size += 1
        return True

    def elimNode(self):
        if self.iterator == self.firstNode:
            if self.lastNode == self.firstNode:
                self.lastNode = None
                self.firstNode = None
                self.iterator = None
            else:
                self.firstNode = self.firstNode.nextNode
                self.firstNode.antNode = None
                self.iterator = self.firstNode
        elif self.iterator == self.lastNode:
            self.lastNode = self.lastNode.antNode
            self.lastNode.nextNode = None
            self.iterator = None
        else:
            self.iterator.antNode.nextNode = self.iterator.nextNode
            self.iterator.nextNode.antNode = self.iterator.antNode
            self.iterator = self.iterator.nextNode
        self.size -= 1
        return True

    def first_Node(self):
        self.iterator = self.firstNode
        return True

    def last_Node(self):
        self.iterator = self.lastNode
        return True

    def nextNode(self):
        if self.iterator:
            self.iterator = self.iterator.nextNode
        return True

    def antNode(self):
        if self.iterator:
            self.iterator = self.iterator.antNode
        return True

    def posNode(self, position):
        if position > 0 and position <= self.size:
            self.iterator = self.firstNode
            for _ in range(1, position):
                self.iterator = self.iterator.nextNode
        else:
            self.iterator = None

    def undefinedIterator(self):
        return self.iterator is None

    def print_list(self):
        if self.size == 0:
            print('Lista vazia')
        else:
            print('Lista:', end=' ')
            current = self.firstNode
            while current is not None:
                print(current.data, end=' ')
                current = current.nextNode
            print()
