class Node:
    def __init__(self, value, next_node = None):
        self.value = value 
        self.next = next_node

    def set_next_node(self, next_node):
        self.next = next_node

    def get_next_node(self):
        return self.next

    def get_value(self):
        return self.value    