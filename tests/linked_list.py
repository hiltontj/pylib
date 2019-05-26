#!/usr/bin/env python3
from .context import data_structs as ds
import unittest

class TestLinkedList(unittest.TestCase):
    def test_strings(self):
        ll = ds.LinkedList()
        ll.push("one")
        ll.push("two")
        ll.push("three")
        self.assertEqual(ll.pop(), "three")
        self.assertEqual(ll.pop(), "two")
        self.assertEqual(ll.pop(), "one")

    def test_access(self):
        ll = ds.LinkedList()
        ll.push("one")
        self.assertEqual(ll.head(), "one")
    
    def test_iteration(self):
        expected = ["one", "two"]
        ll = ds.LinkedList()
        ll.push(expected[0])
        ll.push(expected[1])
        i = len(expected) - 1
        for n in ll:
            self.assertEqual(expected[i], n)
            i = i - 1

if __name__ == "main":
    unittest.main()