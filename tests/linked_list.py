import unittest
from data_structs import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_strings(self):
        ll = LinkedList()
        ll.push("one")
        ll.push("two")
        ll.push("three")
        print("Hi")
        self.assertEqual(ll.pop(), "three")
        self.assertEqual(ll.pop(), "two")
        self.assertEqual(ll.pop(), "one")

if __name__ == "main":
    unittest.main()