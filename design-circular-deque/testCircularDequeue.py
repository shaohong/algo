import unittest
from circularDeque import MyCircularDeque


class TestCircularDeque(unittest.TestCase):

    def test_case_1(self):
        '''
        # MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
        # circularDeque.insertLast(1);			// return true
        # circularDeque.insertLast(2);			// return true
        # circularDeque.insertFront(3);			// return true
        # circularDeque.insertFront(4);			// return false, the queue is full
        # circularDeque.getRear();  			// return 2
        # circularDeque.isFull();				// return true
        # circularDeque.deleteLast();			// return true
        # circularDeque.insertFront(4);			// return true
        # circularDeque.getFront();			// return 4
        '''
        circularDeque = MyCircularDeque(3)
        self.assertEqual(circularDeque.insertLast(1), True)
        self.assertEqual(circularDeque.insertLast(2), True)
        self.assertEqual(circularDeque.insertFront(3), True)
        self.assertEqual(circularDeque.insertFront(4), False)
        self.assertEqual(circularDeque.getRear(), 2)
        self.assertEqual(circularDeque.isFull(), True)
        self.assertEqual(circularDeque.deleteLast(), True)
        self.assertEqual(circularDeque.insertFront(4), True)
        self.assertEqual(circularDeque.getFront(), 4)


if __name__ == '__main__':
    unittest.main()
