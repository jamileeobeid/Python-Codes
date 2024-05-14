class Node:

    def __init__(self, value= None, next=None):
        self.value = value
        self.next = next

class Stack:

    __slots__ = ['top', 'size']

    def __init__(self, top=None, size=0):
        self.top = top
        self.size = size

    def is_empty(self):

        if self.size == 0:
            return True
        
        else:
            return False
        
    def get_size(self):
        return self.size
    
    def push(self, value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size = self.size + 1

    def pop(self):

        deleted_node = self.top.value
        self.top = self.top.next
        self.size = self.size - 1
        return deleted_node
    
def main():

    stack = Stack()

    print("Making sure our stack is empty:", stack.is_empty())
    print("Initially, the size of the stack is:", stack.size)

    print("Adding 10, 20, and 30 to the stack")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Size of the stack after pushing:", stack.size)

    print("removing 2 elements from the stack")
    stack.pop()
    stack.pop()

    print("Size of stack after popping:", stack.size)

main()