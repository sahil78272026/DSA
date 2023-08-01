class Node:
    def __init__(self,value):
        print("New Node Created")
        self.value = value
        self.next = None
        self.pre = None


class DoublyLinkedList:

    def __init__(self,value):
        print("Initializing DLL")
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
        print("Node Appended at the End")
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

        self.length -=1
        print("Node Removed from the End")
        return temp

    # popping out first node from the doubly linked list
    def pop_first(self):
        if self.length ==0:
            return None

        temp = self.head
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.pre = None
            temp.next = None

        self.length -=1
        print("Node Removed from the start")
        return temp



    # adding node at beginning of DLL
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
        print("Node added at the start")
        return True

    # getting value of node at particular index
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:  # checking if index lies in first half of the DLL
            print("Traversing from head")
            for _ in range(index):
                temp = temp.next
        else: # if index lies in second of the DLL, then traverse through tail for more efficiency
            print("Traversing from tail")
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.pre

        print("Getting Node")
        return temp

    # setting value of a prticular node at particular index
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # inserting node at a particular index
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.pre = before
        new_node.next = after
        before.next = new_node
        after.pre = new_node

        self.length+=1
        return True

    # removing a node from a partiulcar index
    def remove(self,index):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        temp = self.get(index)
        temp.next.pre = temp.pre
        temp.pre.next = temp.next
        temp.pre = None
        temp.next = None
        self.length-=1

        return temp


    def print_all(self):
        if self.head is None:
            return None

        pre = self.head
        while pre is not None:
            print(pre.value)
            pre = pre.next

        print('self.length : ', self.length)






doubly_linked_list = DoublyLinkedList(0)
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.append(4)
doubly_linked_list.append(5)
doubly_linked_list.append(6)
doubly_linked_list.print_all()
doubly_linked_list.set_value(2,7)
doubly_linked_list.print_all()
doubly_linked_list.insert(3,9)
#doubly_linked_list.print_all()
#doubly_linked_list.prepend(0)
doubly_linked_list.print_all()
doubly_linked_list.remove(5)
doubly_linked_list.print_all()
#print("Popped Node: ",doubly_linked_list.pop_first().value)
#doubly_linked_list.print_all()
#print(doubly_linked_list.get(3))
#print(doubly_linked_list.get(4))
#doubly_linked_list.print_all()

# 2 items
#print(doubly_linked_list.pop().value)  # printing removed node value

# 1 item
#print(doubly_linked_list.pop())

# 0 Item
#print(doubly_linked_list.pop())

#doubly_linked_list.print_all()