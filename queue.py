class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def peek(self):
        if self.head is None:
            raise IndexError("Черга порожня")
        return self.head.data

    def dequeue(self):
        data = self.peek()
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return data

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def count(self):
        return self.length

    def to_string(self):
        items = ["head"]
        node = self.head
        while node is not None:
            items.append(str(node.data))
            node = node.next
        items.append("null")
        return " -> ".join(items)

    def __str__(self):
        return self.to_string()


if __name__ == "__main__":
    queue = Queue()

    for value in (12, 25, 8):
        queue.enqueue(value)
        print(f"enqueue({value})  ->  {queue}")

    print("\npeek():", queue.peek())
    print("count():", queue.count())
    print("Вивід черги:", queue)

    print("\ndequeue():", queue.dequeue())
    print("Після dequeue:", queue)
    print("count():", queue.count())

    queue.enqueue(40)
    print("\nenqueue(40)  ->", queue)

    print("\nВидаляємо все по черзі:")
    while queue.count() > 0:
        print("  dequeue():", queue.dequeue())
    print("Після видалення:", queue)

    try:
        queue.dequeue()
    except IndexError as error:
        print("\ndequeue() на порожній черзі:", error)