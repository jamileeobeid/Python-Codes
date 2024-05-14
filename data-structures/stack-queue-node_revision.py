#Stack
class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self, top=0, size=0):
        self.top = top
        self.size = size

    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.size == 0:
            return True
        
        else:
            return False
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size = self.size + 1

    def pop(self):
        deleted_node = self.top.value
        self.top = self.top.next
        self.size = self.size -1 
        return deleted_node
    
    def peek(self):
        return self.top.value
    
def main():

    stack = Stack()

    print("Is the stack empty?", stack.is_empty())

    print("Pushing 10, 20, and 30 to the stack")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Size of stack after pushing:", stack.get_size())
    print("Top element:",stack.peek())

    print("Poppping the stack twice")
    stack.pop()
    stack.pop()

    print("Size of stack after popping:", stack.get_size())

    print("Top element:",stack.peek())

main()



#Nodes
class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value
    
    def get_nextNode(self):
        return self.next
    
    def set_nextNode(self,next_node):
        self.next = next_node
        return next_node

def main():

    #creating nodes
    node1 = Node(value=10)
    node2 = Node(value=20)
    node3 = Node(value=30)

    #connecting nodes
    pointer1 = node1.set_nextNode(node2)
    pointer2 = node2.set_nextNode(node3)

    #printing nodes
    print("Node1 value=", node1.get_value())
    print("Node2 value=", node2.get_value())
    print("Node3 value=", node3.get_value())

    #printing the values of node pointers
    print("First node pointer is at:", pointer1.get_value())
    print("Second node pointer is at:", pointer2.get_value())

main()



#Queue
class Queue:

    def __init__(self):
        self.people = []

    def get_size(self):
        return len(self.people)

    def enqueue(self, person):
        self.people.append(person)

    def dequeue(self):
        self.people.pop(0)

def main():

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Size of queue after enqueue:", queue.get_size())

main()