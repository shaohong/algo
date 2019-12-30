# https://leetcode.com/problems/design-circular-deque

class MyCircularDeque:
    DefaultValue = -1
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.items = [MyCircularDeque.DefaultValue] * k
        self.front = -1
        self.end = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False

        if self.count == 0:
            # insert the first item
            self.items[0] = value
            self.front, self.end = 0, 0
        else:
            # adjust the front index
            self.front = (self.front - 1) % self.capacity
            self.items[self.front] = value

        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False

        if self.count == 0:
            # insert the first item
            self.items[0] = value
            self.front, self.end = 0, 0
        else:
            # adjust the end index
            self.end = (self.end +1 ) % self.capacity
            self.items[self.end] = value

        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False

        self.items[self.front] = MyCircularDeque.DefaultValue
        # adjust front index
        self.front = (self.front +1 ) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False

        # adjust end index
        self.items[self.end] = MyCircularDeque.DefaultValue
        self.end = (self.end -1 ) % self.capacity
        self.count -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.items[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.items[self.end]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
