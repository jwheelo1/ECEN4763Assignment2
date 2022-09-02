"""test xor linked list implementation."""

import unittest
import logging
import sys
from structures.linkedlist import linkedlist


class XORListTest(unittest.TestCase):
    """Class Xor List."""

    def setUp(self):
        """Setup."""
        debug = True
        self.linkedlist = linkedlist.XORList()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("LinkedListTestLog")

    def test_linkedlist(self):
        pass
