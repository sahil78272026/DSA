'''
LL: Remove Duplicates (⚡Interview Question)
You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Note: this linked list class does not have a tail which will make this method easier to implement.

Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the remove_duplicates() method in two different ways:



Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.



Here is the method signature you need to implement:

def remove_duplicates(self):


Example:

Input:

LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

Output:

LinkedList: 1 -> 2 -> 3 -> 4 -> 5

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next          

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1



    # WRITE REMOVE_DUPLICATES METHOD HERE #
    #                                     #
    #                                     #
    #                                     #
    #                                     #
    #######################################
    # solution using set, O(n)
    """def remove_duplicates(self):
            values = set()
            previous = None
            current = self.head
            while current:
                if current.value in values:
                    previous.next = current.next
                    self.length -= 1
                else:
                    values.add(current.value)
                    previous = current
                current = current.next"""

    # solution without set, O(n^2)
    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next



my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    4
    
"""
