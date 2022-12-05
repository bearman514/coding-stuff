# import pdb


class Node():

    def __init__(self, data) -> None:
        self.data = data
        self.left = None  # smaller
        self.right = None  # greater

    def __str__(self):
        return """Data: {}""".format(self.data)


class BST():

    def __init__(self):
        self.root = None

    def __str__(self):
        pass

    def inorder_traversal(self):
        """Left -> Root -> Right
        """
        if self.root != None:
            self._inorder_traversal(self.root)
        else:
            print("Empty tree!")

    def _inorder_traversal(self, node):
        if node != None:
            self._inorder_traversal(node.left)
            print(node.data)
            self._inorder_traversal(node.right)

    def preorder_traversal(self):
        """Root -> Left -> Right
        """
        if self.root != None:
            self._preorder_traversal(self.root)
        else:
            print("Empty tree!")

    def _preorder_traversal(self, node):
        if node != None:
            print(node.data)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def postorder_traversal(self):
        """Left -> Right -> Root
        """
        if self.root != None:
            self._postorder_traversal(self.root)
        else:
            print("Empty tree!")

    def _postorder_traversal(self, node):
        if node != None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.data)

    def print_bst(self):
        if self.root != None:
            self._print_bst(self.root)
        else:
            print("Empty tree!")

    def _print_bst(self, curr_node):
        if curr_node != None:
            print("curr", curr_node.data)
            # print("curr left", curr_node.left.data)
            self._print_bst(curr_node.left)
            # pdb.set_trace()
            print(curr_node.data)
            # val = curr_node.data
            self._print_bst(curr_node.right)

    def is_bst(self):
        pass

    def get_min(self):
        if self.root != None:
            return self._get_min(self.root)
        else:
            print("Empty tree!")

    def _get_min(self, node):
        if node != None:
            if node.left != None:
                return self._get_min(node.left)
            else:
                return node.data

    def get_min_node(self):
        if self.root == None:
            return None
        curr = self.root
        while curr.left != None:
            curr = curr.left
        return curr

    def get_max(self):
        if self.root != None:
            return self._get_max(self.root)
        else:
            print("Empty tree!")

    def _get_max(self, node):
        if node != None:
            if node.right != None:
                return self._get_max(node.right)
            else:
                return node.data

    def get_height(self):
        pass

    def get_level(self):
        pass

    def find(self, value):
        if self.root == None:
            print("Empty tree!")
        else:
            is_exist = self._find(value, self.root)
            if is_exist:
                print(f"Found: {value}")
            else:
                print(f"Not found: {value}")

    def _find(self, value, node):
        if node != None:
            if value < node.data:
                # search left
                return self._find(value, node.left)
            elif value > node.data:
                # search right
                return self._find(value, node.right)
            else:
                return True

    def next_element(self):
        pass

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._instert(value, self.root)

    def _instert(self, value, curr_node):
        if value < curr_node.data:
            # left
            if curr_node.left == None:
                curr_node.left = Node(value)
            else:
                self._instert(value, curr_node.left)
        elif value > curr_node.data:
            # right
            if curr_node.right == None:
                curr_node.right = Node(value)
            else:
                self._instert(value, curr_node.right)
        else:
            raise Exception

    def delete(self, value):
        if self.root == None:
            print("Empty tree")
        else:
            self._delete(value, self.root)

    def _delete(self, value, node):
        if node.date == value:

            # case 1
            if node.left == None and node.right == None:
                pass

    def delete_tree(self):
        pass


if __name__ == "__main__":

    bst = BST()

    for i in [10, 12, 9, 5, 6]:
        bst.insert(i)

    # print("In-order")
    # bst.inorder_traversal()

    # print("Pre-order")
    # bst.preorder_traversal()

    # print("Post-order")
    # bst.postorder_traversal()

    # bst.find(50)

    min_num = bst.get_min()
    print(min_num)
    max_num = bst.get_max()
    print(max_num)

    min_node = bst.get_min_node()
    print(min_node)
