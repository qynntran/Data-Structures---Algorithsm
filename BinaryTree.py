class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_tree(self, values):
        for value in values:
            self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, current_node):
        if current_node is not None:
            print(current_node.value, end=' ')
            self._preorder_recursive(current_node.left)
            self._preorder_recursive(current_node.right)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        if current_node is not None:
            self._inorder_recursive(current_node.left)
            print(current_node.value, end=' ')
            self._inorder_recursive(current_node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, current_node):
        if current_node is not None:
            self._postorder_recursive(current_node.left)
            self._postorder_recursive(current_node.right)
            print(current_node.value, end=' ')


def main():
    tree = BinaryTree()

    # Tạo cây nhị phân
    tree.create_tree([27, 14, 35, 10, 19, 31])
    tree.insert(42)

    # Duyệt cây theo thứ tự Preorder
    print("Preorder traversal:")
    tree.preorder_traversal()
    print()

    # Duyệt cây theo thứ tự Inorder
    print("Inorder traversal:")
    tree.inorder_traversal()
    print()

    # Duyệt cây theo thứ tự Postorder
    print("Postorder traversal:")
    tree.postorder_traversal()
    print()

if __name__ == '__main__':
    main()
