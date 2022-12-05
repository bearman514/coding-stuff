"""_summary_

Resourdes:
https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK

"""


class Node():

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self):
        return "Data: {}".format(self.data)


class SingleLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):

        data_str = ""
        ll = self.head
        while ll:
            data_str += str(ll.data) + ", "
            ll = ll.next
        return "[" + data_str + "]"

    def __len__(self):
        k = 0
        ll = self.head
        while ll:
            k += 1
            ll = ll.next
        return k

    def get_topFront(self):
        return self.head.data if self.head else None

    def get_topBack(self):
        return self.tail.data if self.tail else None

    def get_node(self, data):
        if self.find(data):
            item = self.head
            while True:
                if item.data == data:
                    return item
                item = item.next

    def push_front(self, data):
        """Add to front
        Time space: O(1)
        """
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    def pop_front(self):
        """Remove front item
        Time space: O(1)
        """
        if self.head == None:
            print("Add a item first!")
            return
        self.head = self.head.next
        # Last one
        if self.head == None:
            self.tail = None

    def push_back(self, data):
        """Add to back
        If no tail:
            Time space: O(n) [Go through front to the back]
        With tail:
            Time space: O(1)
        """
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        # Only one
        if self.head == None:
            self.head = new_node

    def pop_back(self):
        """Remove back item
        If no tail:
            Time space: O(n) [Go through front to the back]
        With tail:
            Time space: O(n)
        """

        if self.head == None:
            print("Add a item first!")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            item = self.head
            while item.next.next:
                item = item.next
            item.next = None
            self.tail = item

    def find(self, data) -> bool:
        """Is key in list
        Time space: O(n)
        """
        item = self.head
        if item == None:
            print("Add a item first!")
            return False

        while item:
            if item.data == data:
                print("Find data: {}".format(data))
                return True
            item = item.next

        print("Not in linked list !")
        return False

    def erase(self, data):
        """Remove data from linked list
        Time space: O(n)
        Tips: Dummy head
        """
        dummy_head = Node(None)
        dummy_head.next = self.head
        curr = dummy_head

        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
            else:
                curr = curr.next

            if curr.next == None:
                self.tail = curr

        self.head = dummy_head.next

    def add_after(self, node, data):
        """
        Time space: O(n)
        """
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        if self.tail == node:
            self.tail = new_node

    def add_before(self, node, data):
        """Adds data before node
        Time space: O(n)
        """
        new_node = Node(data)
        new_node.next = node
        #
        if self.head == node:
            self.head = new_node
        else:
            item = self.head
            while item.next != node:
                item = item.next
            item.next = new_node

    def reverse(self):
        pre, curr, next = None, self.head, None
        while curr != None:
            next = curr.next
            curr.next = pre
            pre, curr = curr, next
        self.head = pre
        self.tail = curr


if __name__ == "__main__":

    sll = SingleLinkedList()

    length = len(sll)

    print(length)

    lst = [1, 2, 1, 1]

    for ele in lst:
        sll.push_back(ele)

    sll.erase(1)

    print(sll)

    print(sll.head)
    print(sll.tail)
