
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None # will point towards next node


class LinkedList:

    #Constructor
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node # pointers towards nodes
        self.tail = new_node # pointers towards nodes
        self.length = 1 # lenght of linked list
        print("Node Created with Value :", new_node.value)

    # getting node at given index
    def get(self,index):
        print(f"Getting Value from given index")
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # setting/changing value of a node at particular index
    def set_value(self,index,value):
        print(f"Setting value:{value} at Index:{index}")
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index) # we can also call self.get(index) method and that will return the node istead of below 3 lines
        if temp:
            temp.value = value
            return True
        """temp = self.head
        for _ in range(index):
            temp = temp.next"""
            
        return False
    # Inserting new node at a given index
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index==0: # if index is zero, we already have method to insert at first position
            return self.prepend(value)
        if index == self.length: # if index is equal to lenght, we already have method to insert at last position
            return self.append(value)

        temp = self.get(index-1) # getting one node before where we have to insert the new node
        new_node = Node(value)
        new_node.next = temp.next 
        temp.next = new_node
        self.length+=1
        print("New Node Inserted....")
        return True

    # removing a node from particular index
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index==0: # if index is zero, we already have method to remove from first position
            return self.pop_first()
        if index == self.length-1: # if index is equal to lenght, we already have method to remove from last position
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length-=1
        print("Node Removed....")
        return temp
        
    
    # adding new node at the end of the linked list
    def append(self,value):
        new_node = Node(value)
        if self.head is None: # checking if linked list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        print("Node appended with Value :", new_node.value)
        return True

        
    # popping out last element from Linked List
    def pop(self):
        # checking if lenght of linkedlist is 0
        if self.length==0:
            return None
        # temporary variables for traversing through the linkedlist
        temp = self.head 
        pre =  self.head

        while (temp.next): # start traversing from beginning and checking if next attribute of node is pointing to last element or note
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length-=1
        if self.length==0:
            self.head = None
            self.tail = None
        print("Node Removed from Last Position")
        return temp.value
    
    # adding new node at the beginning of the linked list
    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # pointing head to new node next attribute
            self.head = new_node # pointing new node to head
        self.length+=1
        return True

    # removing first node
    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length==0: # when linkedlist having one node
            self.tail=None

        return temp.value  # return entire node instead

    # reversing a linked list, very important interview question
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        

    # print all vlaues of linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print("Node Value: ", temp.value)
            temp = temp.next
        
        print('Lenght of Linked List: ',self.length)

    
 
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
#my_linked_list.remove(2)
my_linked_list.reverse()

#my_linked_list.set_value(2,8)
#print(my_linked_list.get(2))
my_linked_list.print_list()

# 2 items
#print(my_linked_list.pop_first())

# 1 item
#print(my_linked_list.pop_first())

# 0 Item
#print(my_linked_list.pop_first())

#my_linked_list.prepend(1)


# 2 items
#print(my_linked_list.pop())

# 1 item
#print(my_linked_list.pop())

# 0 Item
#print(my_linked_list.pop())

'''
print('Node:', my_linked_list.head)
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
'''


                                                                                                                    