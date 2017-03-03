from PythonADT.lists import LinkedList

class Stack(object):
    
    def __init__(self):
    """
    Initializes the stack by creating a LinkedList
    """
        self.__items = LinkedList()
    
    def push(self, v):
    """
    Pushes the item onto the stack by adding an item to 
    the beginning of the linked list
    """
        self.__items.insert(v)
    
    def pop(self):
    """
    Removes the first item from the linked list and returns it;
    If list is empty, returns None
    """
        if self.__items.head:
            item = self.__items.head
            self.__items.head = self.__items.head.next
            return item.value
        else:
            return None
        
    def peek(self):
    """
    Looks at the value of the first item on the stack 
    without removing it
    """
        return self.__items.head.value
        
    def isEmpty(self):
    """
    Checks if the stack is empty
    """
        return self.__items.size() == 0
        
    def size(self):
    """
    Returns the number of items currently on the stack
    """
        return self.__items.size()
        
    def __str__(self):
    """
    Prints the contents of the stack by printing the underlying
    linked list
    """
        return self.__items.__str__()
    
       
        