class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def sort(self):
        # Convert the linked list into a regular Python list
        queue_list = []
        current = self.front
        while current:
            queue_list.append(current.data)
            current = current.next

        # Sort the Python list
        queue_list.sort()

        # Rebuild the queue using the sorted list
        self.front = self.rear = None
        for item in queue_list:
            self.enqueue(item)


# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(8)
    q.enqueue(1)
    q.enqueue(6)

    print("Original Queue:")
    q.display()

    print("\nDequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())

    print("\nQueue after dequeue:")
    q.display()

    q.enqueue(10)
    q.enqueue(2)

    print("\nQueue after enqueue:")
    q.display()

    q.sort()

    print("\nQueue after sorting:")
    q.display()
