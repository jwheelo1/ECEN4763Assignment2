# Data Structures XOR Linked List

An XOR linked list is a memory efficient doubly linked list. It has addresses to the previous and the next node in the list. Instead of storing the addresses, it stores the XOR of the previous and the next addresses. However, it is more complex and hard to debug.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format" will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# XOR Linked List

## Requirements

- You must implement a class that handles the below interfaces for an xor list.
- The class name must be called "XORList".
- Will have another class called "Node"
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style".
- Your unit tests must reach 100% code coverage

## Interface

### Node Class
- The helper Node class must contain two variables: value and xor_addr. The xor_addr will contian the address of the next node xor'd with the address of the previous node.
- The function get_address(self) should simply return id(self)
- The function get_value(self) should return the value stored in the Node

### XORList Class
- The constructor __init__(self, array=None) initializes the head and tail variables to None. Because Python will delete objects that are only referenced by their address, we also must initialize a set of Nodes in the list. Please do not directly use this set, it is only included so that the Nodes don't get deleted. The passed array variable can be used to populate the list, adding the nodes in order using self.insert_end.
- The function get_head(self) gets the head pointer of the linked list.
- The function get_tail(self) gets the tail pointer of the linked list.
- The function insert_begin(self, value) inserts a node storing value at the head of the linked list, updating any necessary addresses.
- The function insert_end(self, value) inserts a node stroing value at the end (tail) of the linked list, updating any necessary addresses.
- The function insert_before(self, next_value, value) inserts a node storing value before the first node found containing the value next_value. If next_value is not found, do nothing.
- The function insert_after(self, prev_value, value) inserts a node storing value after the first node found containing the value prev_value. If prev_value is not found, do nothing.
- The function find(self, value) returns true if value is in list and false if value is not in list.
- The function length(self) returns the length of the linked list, returns 0 if the list is empty.
- The function get_array(self) returns an array containing the elements in the xorlist, from head to tail. You must do this by stepping through the list, not by returning some previously stored array.
- The function is_empty(self) returns true if the linked list is empty and false if the list is not empty.
- The function delete_head(self) deletes the head of the linked list.
- The function delete_tail(self) deletes the tail of the linked list.
- The function delete_node(self, value) deletes the first node containing value. It should return value if successful, and None if not.
- The function empty_list(self) deletes the entire linked list.

### Helper Functions (Outside of Class)
- The function type_cast(address) converts an address address into a python object using the following code: return ctypes.cast(address, ctypes.py_object).value
- The function xor(xor_a, xor_b) returns the xor of the inputs xor_a and xor_b
- The function get_space_complexity(), returns the space complexity of the data structure
- The function get_time_complexity(), returns the time complexity of find based on the number of elements in the list

## Pointers
- I am including some helpful tips in this section so that you can all have an easier time on this assignment.
- You can step through the list by keeping track of a previous address (initialized to 0) and a current Node object (initialized to self.head)
- The next address can be found by using xor(prev, curr.xor_addr)
- Once the next address is found, prev can be updated to curr.get_address() and curr can be updated to type_cast(next)
- The tail is reached when curr is tail
- Similar methods of extracting the previous and next addresses from each Node using xor can be used to update the addresses when inserting and deleting.

## Tests

- Check insertion and deletion this includes all the different ways to insert and delete (i.e. beginning, end, before, after)
- Check insertion of repeated values
- Check double deletion of values
- Check if value is present in list or not
- Check length of list
- Check the time complexity of the data structure
- Check that as you insert nodes they insert into the correct places in the list 

## Corner Cases

- Delete when list is empty
- Insert before or after a value that is not in the list 
- Insert before the head or after the tail

## Library

You can only use basic python libraries (no special imports).
