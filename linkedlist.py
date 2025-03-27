from node import *


class LinkedList:
    def __init__(self, value = None):
        self.head = Node(value)  # Die Liste beginnt mit keinem Element (head ist None)

    def get_head_node(self):
        return self.head

    def append(self, value):
        """Fügt einen neuen Knoten am Ende der Liste hinzu."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node  # Wenn die Liste leer ist, wird der neue Knoten zum Kopf
        else:
            last_node = self.head
            while last_node.next:  # Gehe bis zum letzten Knoten
                last_node = last_node.next
            last_node.next = new_node  # Der letzte Knoten zeigt auf den neuen Knoten

    def prepend(self, value):
        """Fügt einen neuen Knoten am Anfang der Liste hinzu."""
        new_node = Node(value)
        new_node.set_next_node(self.head)  # Der neue Knoten zeigt auf das bisherige erste Element
        self.head = new_node  # Der Kopf der Liste zeigt jetzt auf den neuen Knoten

    def delete(self, value):
        """Löscht den ersten Knoten mit dem angegebenen Wert."""
        current = self.head
        if current and current.value == value:
            self.head = current.next  # Wenn der Kopf gelöscht wird, wird der nächste Knoten zum neuen Kopf
            current = None
            return

        prev = None
        while current and current.value != value:
            prev = current
            current = current.next

        if current is None:  # Der Wert wurde nicht gefunden
            print(f"Wert {value} nicht in der Liste gefunden.")
            return

        prev.next = current.next  # Der vorherige Knoten zeigt nun auf das nächste Element
        current = None  # Der Knoten wird gelöscht

    def search(self, value):
        """Sucht nach einem Knoten mit dem angegebenen Wert und gibt ihn zurück."""
        current = self.head
        while current:
            if current.value == value:
                return current  # Wert gefunden
            current = current.next
        return None  # Wert nicht gefunden

    def display(self):
        """Gibt die Werte aller Knoten in der Liste aus."""
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print(" -> ".join(map(str, values)))