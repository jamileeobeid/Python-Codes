class Queue:

    def __init__(self):
        self.people = []

    def is_empty(self):

        if len(self.people) == 0:
            return True
        
        else:
            return False
        
    def get_size(self):
        return len(self.people)
    
    def enqueue(self, person):
        self.people.append(person)
    
    def dequeue(self):
        self.people.pop(0)

def main ():

    MyQueue = Queue() #creating a queue

    #adding elements to the queue
    MyQueue.enqueue(10)
    MyQueue.enqueue(20)

    print("The size of the queue after enqueue:", MyQueue.get_size())

    MyQueue.dequeue() #removing one element from the queue

    print("The size of the queue after dequeue:", MyQueue.get_size())

    print("Is the queue empty? ", MyQueue.is_empty())

main()

