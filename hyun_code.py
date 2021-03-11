class Node:
    def __init__(self, data, left=None, right=None):
        super().__init__()
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if data < 0:
            return print('** ', data, '는 음수 값 입니다. 양수만 입력 가능합니다.')

        self.root = self._insert_value(self.root, data)

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node

    # 출력
    def _callback(self, value):
        print(value, end=' ')

    def _pre_order(self, node):
        if node != None:
            self._callback(node.data)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def _in_order(self, node):
        if node != None:
            self._in_order(node.left)
            self._callback(node.data)
            self._in_order(node.right)

    def _post_order(self, node):
        if node != None:
            self._post_order(node.left)
            self._post_order(node.right)
            self._callback(node.data)



bst = BinarySearchTree()
tempArray = [10, 11, 4, 2, 1, 3, 7, 5, 6]

for item in tempArray:
    bst.insert(item)

bst._pre_order(bst.root)
# bst._in_order(bst.root)
# bst._post_order(bst.root)