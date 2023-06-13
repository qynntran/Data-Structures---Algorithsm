class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = current

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < position:
                current = current.next
                count += 1
            if current:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
            else:
                raise IndexError("Invalid position")

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        current = self.head
        while current and current.data != data:
            current = current.next

        if current:
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

    def search(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        return current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    linked_list = DoublyLinkedList()

    # Thêm phần tử vào cuối danh sách
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    # Hiển thị danh sách liên kết
    print("Danh sách liên kết:")
    linked_list.display()

    # Xoá phần tử 2 khỏi danh sách
    linked_list.delete(2)

    # Hiển thị danh sách liên kết sau khi xoá
    print("Danh sách liên kết sau khi xoá:")
    linked_list.display()

    # Tìm phần tử 3 trong danh sách
    node = linked_list.search(3)
    if node:
        print("Phần tử 3 được tìm thấy")
    else:
        print("Phần tử 3 không tồn tại")

    # Thêm phần tử 5 vào vị trí thứ 1
    linked_list.insert(5, 1)

    # Hiển thị danh sách liên kết sau khi thêm
    print("Danh sách liên kết sau khi thêm:")
    linked_list.display()

if __name__ == '__main__':
    main()
