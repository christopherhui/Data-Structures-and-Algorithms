class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self, initdata):
        return str(initdata)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        aList = []
        node = self.head
        while node != None:
            aList = aList + [node.getData()]
            node = node.getNext()

        return str(aList)

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        last = self.head
        if last == None:
            self.head = temp
        else:
            while last.getNext() != None:
                last = last.getNext()
            last.setNext(temp)

    def insert(self, item, place):
        temp = Node(item)
        prev = None
        current = self.head

        for i in range(0, place):
            prev = current
            current = current.getNext()

        prev.setNext(temp)
        temp.setNext(current)

    def index(self, place):
        current = self.head
        for i in range(0, place):
            current = current.getNext()

        return current.getData()

    def pop(self, place):
        prev = None
        current = self.head
        for i in range(0, place):
            prev = current
            current = current.getNext()

        prev.setNext(current.getNext())
        return current.getData()


mylist = UnorderedList()

mylist.add(54)
mylist.append(10)
mylist.insert(21, 2)

print(mylist.size())
print(mylist.index(2))
print(mylist)
print(mylist.pop(1))
print(mylist)
