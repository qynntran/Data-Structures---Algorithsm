class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print("Stack:", self.items)


def main():
    stack = Stack()

    # Thêm phần tử vào stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    # In stack
    stack.print_stack()

    # Pop phần tử từ stack
    item = stack.pop()
    print("Pop item:", item)

    # In stack sau khi pop
    stack.print_stack()

    print("Peek: ", stack.peek())

if __name__ == '__main__':
    main()
