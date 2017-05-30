class BigInteger:
    """
    Create new Big Integer object
    """
    def __init__(self, initValue = ""):
        self._head = None
        self._tail = None
        self.length = 0
        for val in initValue:
            self.addNode(val)
            self.length += 1

    # Helper method for appending terms to the Big Integer.
    def addNode(self, val):
        val = int(val)
        newNode = _TermNode(val)
        if self._head is None:
            self._head = newNode
        else:
            newNode.prev = self._tail
            self._tail.next = newNode
        self._tail = newNode

    def toString(self):
        """
        :return: Big Integer as string
        """
        currNode = self._head
        s = ""
        while currNode is not None:
            s += str(currNode.initValue)
            currNode = currNode.next
        return s

    def __lt__(self, other):
        """
        :param other: big integer
        :return: bool
        """
        currNode = self._head
        otherNode = other._head

        if self.length > other.length:
            return False
        elif self.length < other.length:
            return True

        while currNode is not None and otherNode is not None:
            if int(currNode.initValue) > int(otherNode.initValue):
                return False
            elif int(currNode.initValue) < int(otherNode.initValue):
                return True
            currNode = currNode.next
            otherNode = otherNode.next

        return None

    def __add__(self, other):
        """
        :param other: Big Integer
        :return: sum of two Big Integers
        """

        diff = abs(self.length - other.length)
        newBigInteger_temp = BigInteger()
        newOther = BigInteger()
        newBigInteger = BigInteger()
        currNode = self._head
        otherNode = other._head
        rem = 0

        if self.length > other.length:
            for item in range(diff):
                newOther.addNode("0")

            while otherNode is not None:
                newOther.addNode(otherNode.initValue)
                otherNode = otherNode.next

            otherNode = self._tail
            newOtherNode = newOther._tail


        if self.length <= other.length:
            for item in range(diff):
                newOther.addNode("0")

            while currNode is not None:
                newOther.addNode(currNode.initValue)
                currNode = currNode.next

            otherNode = other._tail
            newOtherNode = newOther._tail

        while otherNode is not None:
            s = int(otherNode.initValue) + int(newOtherNode.initValue)
            if s % 10 > 0:
                if (s % 10 + rem) > 10:
                    newBigInteger_temp.addNode((s % 10 + rem) % 10)
                    rem += 1
                else:
                    newBigInteger_temp.addNode(s % 10 + rem)
                    rem = 0
            else:
                newBigInteger_temp.addNode(s % 10 + rem)
                rem = 0
            newOtherNode = newOtherNode.prev
            otherNode = otherNode.prev
        newBigInteger_temp = newBigInteger_temp._tail

        while newBigInteger_temp is not None:
            newBigInteger.addNode(newBigInteger_temp.initValue)
            newBigInteger_temp = newBigInteger_temp.prev

        return newBigInteger.toString()
    
    
    def __sub__(self, other):
        """
        :param other: Big Integer
        :return: sublime of two Big Integers
        """

        diff = abs(self.length - other.length)
        newBigInteger_temp = BigInteger()
        newOther = BigInteger()
        newBigInteger = BigInteger()
        currNode = self._head
        otherNode = other._head
        rem = 0
        check = False

        if int(self.toString()) >= int(other.toString()):
            for item in range(diff):
                newOther.addNode("0")

            while otherNode is not None:
                newOther.addNode(otherNode.initValue)
                otherNode = otherNode.next

            otherNode = self._tail
            newOtherNode = newOther._tail


        if self.length <= other.length:
            for item in range(diff):
                newOther.addNode("0")

            while currNode is not None:
                newOther.addNode(currNode.initValue)
                currNode = currNode.next

            otherNode = other._tail
            newOtherNode = newOther._tail
            check = True

        while otherNode is not None:
            s = int(otherNode.initValue) - int(newOtherNode.initValue)
            if s > 0:
                if (s % 10 + rem) > 10:
                    newBigInteger_temp.addNode((s % 10 + rem) % 10)
                    rem += 1
                else:
                    newBigInteger_temp.addNode(s % 10 + rem)
                    rem = 0
            else:
                newBigInteger_temp.addNode(s % 10 + rem)
                rem += 1
            newOtherNode = newOtherNode.prev
            otherNode = otherNode.prev
        newBigInteger_temp = newBigInteger_temp._tail

        while newBigInteger_temp is not None:
            newBigInteger.addNode(newBigInteger_temp.initValue)
            newBigInteger_temp = newBigInteger_temp.prev

        if check:
            return "-" + newBigInteger.toString()
        else:
            return newBigInteger.toString()


    def __str__(self):
        currNode = self._head
        s = ""
        while currNode is not None:
            s += str(currNode.initValue) + "-> "
            currNode = currNode.next
        return s

# Class for creating Big Integer term nodes used with the linked list.
class _TermNode:

    def __init__(self, initValue):
        self.initValue = initValue
        self.next = None
        self.prev = None


'''
a = BigInteger("1001")
b = BigInteger("1000")
print("a =", a.toString())
print("b =", b.toString())
print(b > a)
print(a + b)
'''
