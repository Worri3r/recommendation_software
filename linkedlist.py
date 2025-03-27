from node import *


class LinkedList:
    def __init__(self, value = None):
        self.head = Node(value)  # linkedlist first has a Node with value of None

    def get_head_node(self):
        return self.head

    def insert(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node

    def delete(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next  # if the head gets deleted, the next node becomes the new head
            current = None
            return

        prev = None
        while current and current.value != value:
            prev = current
            current = current.next

        if current is None:
            print(f"Wert {value} nicht in der Liste gefunden.")
            return

        prev.next = current.next  # previous node points to the next node
        current = None  # node gets deleted

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current  # value found
            current = current.next
        return None  # value not found

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print(" -> ".join(map(str, values))) # displays all values of all nodes