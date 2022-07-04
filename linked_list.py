class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node('head')

    def find(self, item):
        current_node = self.head
        while current_node.data != item:
            current_node = current_node.next
        return current_node

    def insert(self, item, new):
        new_node = Node(new)
        current_node = self.find(item)
        new_node.next = current_node.next
        current_node.next = new_node
        current_node.next.previous = new_node
        current_node.next = new_node
        new_node.previous = current_node

    def show(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data, end=' - ')
            current_node = current_node.next
        print(current_node.data)

    def remove(self, item):
        current_node = self.find(item)

        if not current_node.next:
            current_node.previous.next = None

        elif current_node.previous.data == 'head':
            current_node.next.previous = self.head
            self.head.next = current_node.next

        else:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous

    def find_last(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def show_reverse(self):
        current_node = self.find_last()
        while current_node.previous:
            print(current_node.data, end=' - ')
            current_node = current_node.previous
        print(current_node.data)


ll = DoublyLinkedList()
ll.insert('head', '1')
ll.insert('1', '2')
ll.insert('2', '3')
ll.insert('3', '4')
ll.show()
ll.remove('4')
ll.show()
ll.show_reverse()
