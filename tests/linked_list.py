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

if __name__ == "main":
    unittest.main()