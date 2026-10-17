

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        print(data, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Popped:", self.top.data)
            self.top = self.top.next

    def display(self):
        current = self.top
        print("Stack:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        print(data, "added to queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Removed:", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        current = self.front
        print("Queue:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


stack = Stack()
queue = Queue()

stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.dequeue()
queue.display()
