class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def print_queue(self):
        print("Queue:", self.items)


def main():
    queue = Queue()

    # Thêm phần tử vào hàng đợi
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    # In hàng đợi
    queue.print_queue()

    # Loại bỏ phần tử từ hàng đợi
    item = queue.dequeue()
    print("Removed item:", item)

    # In hàng đợi sau khi loại bỏ phần tử
    queue.print_queue()

if __name__ == '__main__':
    main()
