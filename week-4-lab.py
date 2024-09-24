class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Empty stack")
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Empty stack")
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Empty queue")
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Empty queue")
    
    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            print("Empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, item):
        inserted = False
        for i in range(len(self.queue)):
            if self.queue[i][0] < priority:
                self.queue.insert(i, (priority, item))
                inserted = True
                break
        if not inserted:
            self.queue.append((priority, item))

    def dequeue(self):
        if self.is_empty():
            return "Priority queue is empty"
        return self.queue.pop(0)[1]

    def peek(self):
        if self.is_empty():
            return "Priority queue is empty"
        return self.queue[0][1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)



def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target :
            left = mid + 1
        else:
            right = mid - 1
        
    return -1
  
def main():
    # Stack Operations
    print("Stack Operations:")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack top:", stack.top())  
    print("Stack size:", stack.size()) 
    stack.pop()
    print("Stack top after pop:", stack.top()) 
    print("Is stack empty?", stack.is_empty())  
    print()

    # Queue Operations
    print("Queue Operations:")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue front:", queue.front())  
    print("Queue rear:", queue.rear()) 
    print("Queue size:", queue.size())  
    queue.dequeue()
    print("Queue front after dequeue:", queue.front()) 
    print("Is queue empty?", queue.is_empty())  
    print()

    # Priority Queue Operations
    print("Priority Queue Operations:")
    priority_queue = PriorityQueue()
    priority_queue.enqueue(3, 'Task A')
    priority_queue.enqueue(1, 'Task B')
    priority_queue.enqueue(5, 'Task C')
    priority_queue.enqueue(2, 'Task D')
    print("Element with highest priority:", priority_queue.peek())
    priority_queue.dequeue()
    print("Element with next highest priority:", priority_queue.peek())  
    print("Is priority queue empty?", priority_queue.is_empty())  
    print("Priority queue size:", priority_queue.size()) 
    print()

    # Binary Search
    print("Binary Search:")
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")

if __name__ == "__main__":
    main()
