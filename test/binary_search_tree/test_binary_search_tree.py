"""test binary search tree implementation."""


import unittest
import logging
import sys
from structures.binary_search_tree import binary_search_tree


class BSTreeTest(unittest.TestCase):
    """Class BSTreeTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.btree = binary_search_tree.Node(20)

        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("BTreeTestLog")

    def test_bs_tree(self):
        pass
