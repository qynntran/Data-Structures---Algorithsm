class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, index):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Invalid index")
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        while self.head is not None and self.head.data == data:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
            else:
                current = current.next

    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    linked_list = LinkedList()

    # Thêm phần tử vào cuối danh sách
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(4)

    # Hiển thị danh sách liên kết
    print("Danh sách liên kết:")
    linked_list.display()

    # Xoá phần tử 2 khỏi danh sách
    linked_list.delete(2)

    # Hiển thị danh sách liên kết sau khi xoá
    print("Danh sách liên kết sau khi xoá:")
    linked_list.display()


if __name__ == '__main__':
    main()
