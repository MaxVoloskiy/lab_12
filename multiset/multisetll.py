from node import *        

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def __len__(self):
        res = 0
        current = self._head
        while current is not None:
            res += 1
            current = current.next
        return res

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        self._head = None

    def split_half(self):
        id = 0
        ml1 = Multiset()
        ml2 = Multiset()
        current = self._head

        half_pos = len(self) / 2
        while current is not None:
            id += 1
            if id <= half_pos:
                ml1.add(current.item)
            else:
                ml2.add(current.item)
            current = current.next
        print(len(ml1), len(ml2))
        return ml1._head, ml2._head

if __name__ == "__main__":
    m = Multiset()
    m.add(11)
    m.add(123)
    m.add(145)
    m.add("Yabluko")
    print(len(m))
    m.split_half()