class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre = None
        

class DoublyLinkedList:

    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # adding new node at the end the linked list
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
        self.length+=1
        return True

    # popping out last node from the doubly linked list
    def pop(self):
        if self.length ==0:
            return None
        
        temp = self.tail

        if self.length==1:
            self.head = None
            self.tail = None
        
        else:
            self.tail = self.tail.pre
            self.tail.next = None
            temp.pre = None

        self.length-=1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.length+=1
        return True
        


    
    def print_all(self):
        if self.head is None:
            return None
        
        pre = self.head
        while pre is not None:
            print(pre.value)
            pre = pre.next
            
        print('self.length : ',self.length)

    

        


doubly_linked_list = DoublyLinkedList(4)
doubly_linked_list.append(8)
doubly_linked_list.append(7)
doubly_linked_list.append(9)
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.print_all()
doubly_linked_list.prepend(3)
doubly_linked_list.print_all()

# 2 items
#print(doubly_linked_list.pop().value)  # printing removed node value

# 1 item
#print(doubly_linked_list.pop())

# 0 Item
#print(doubly_linked_list.pop())

#doubly_linked_list.print_all()