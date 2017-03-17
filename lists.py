class LinkedList(object):
    class Node(object):
        """
        Inner class of LinkedList. Contains a blueprint for a node of the LinkedList
        """
        def __init__(self, _value, _next=None):
            """
            Initializes a List node with payload v and link n
            """
            self.value = _value
            self.next = _next
        
        def __eq__(self,other):
            """
            Defining comparison between nodes for unit testing
            """
            return self.value == other.value and self.next == other.next
         
    def __init__(self):
        """
        Initializes a LinkedList and sets list head to None
        """
        self.head=None
        self.__current=self.head
        
    def __len__(self):
        """
        Returns the current size of the list. O(n), linear time
        """ 
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
        
    def __contains__(self,value):
        """
        Returns True or False depending on whether an item with
        node.value = value is in the list 
        """
        current = self.head
        found = False
        while current and not found:
            if current.value == value:
                return True
            current = current.next
        return False 
                
    def __iter__(self):
        """
        Creates an iterator. Returns itself.
        """
        return self
            
    def __next__(self):
        """
        Provides the next entry to the iterator
        """
        if not self.__current:
            self.__current=self.head
            raise StopIteration
        current = self.__current
        self.__current=self.__current.next
        return current
            
    def __str__(self):
        """
        Prints the current list in the form of a Python list            
        """
        current = self.head
        to_print = []
        while current:
            to_print.append(current.value)
            current = current.next
        return str(to_print)      
         
    def insert(self, value, position=0):
        """
        Adds an item with payload v to beginning of the list
        in O(1) time or to position in the list in O(n) time 
        """
        if value is None:
            raise ValueError('Cannot add None item to a list')
        if position < 0:
            raise ValueError('Cannot add to negative position in the list')
        if position == 0:
            self.node = self.Node(value, self.head)
            self.head = self.node
            self.__current=self.head
            return self.node
        else:
            current = self.head
            count = 0
            while current and ((count+1)<=position):
                #found the position to insert into
                if count + 1 == position:
                    self.node = self.Node(value, current.next)
                    current.next = self.node
                    return self.node
                else:
                    current = current.next
                    count += 1
            if not current:
                return None
    
    def search(self, value):
        """
        Searches the list for a node with payload v. Returns the node object or None if not found. Time complexity is O(n) in worst case.
        """
        current = self.head
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:    
                current = current.next
        if not current:
            return None
        return current
        
    def delete(self, value):
        """
        Searches the list for a node with payload v. Returns the node object or None if not found. Time complexity is O(n) in worst case.
        """
        if value is None:
            raise ValueError('Cannot remove None item from the list')
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next
        # nothing found, return None
        if not current:
            return None
        # the case where first item is being deleted
        if not previous:
            self.head = current.next
        # item from inside of the list is being deleted    
        else:
            previous.next = current.next
             
        return current
        
        
class DLinkedList(object):
    _size = 0
    class Node(object):
        def __init__(self, _value, _previous, _next):
            self.value = _value
            self.next = _next
            self.previous = _previous
            
        def __eq__(self, other):
            return (self.value == other.value) and (self.next == other.next) and (self.previous == other.previous)
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0        
        
    def __len__(self):
        if self.head:
            return self._size
        else:
            return 0
            
    def __str__(self):
        current = self.head
        to_print = []
        while current:
            to_print.append(current.value)
            current = current.next
        return str(to_print)
        
    def __iter__(self):
        """
        Creates an iterator. Returns itself.
        """
        return self
            
    def __next__(self):
        """
        Provides the next entry to the iterator
        """
        if not self.__current:
            self.__current=self.head
            raise StopIteration
        current = self.__current
        self.__current=self.__current.next
        return current
    
    def __contains__(self,value):
        """
        Returns True or False depending on whether an item with
        node.value = value is in the list 
        """
        current = self.head
        found = False
        while current and not found:
            if current.value == value:
                return True
            current = current.next
        return False    
        
    def insert(self, _value, _position=0, _previous = None, _next = None):
        if _value is None:
            raise ValueError('Cannot add None item to a list')
        if _position < 0:
            raise ValueError('Cannot add to negative position in the list')
        if _position == 0:
            if self.head:
                new_node = self.Node(_value, None, self.head)
                old_node = self.head
                self.head = new_node
                old_node.previous = new_node
                self._size = self._size + 1
            else:
                new_node = self.Node(_value, None, None)
                self.tail = new_node
                self.head = new_node
                self._size = self._size + 1
            return new_node
        else:
            current = self.head
            count = 0
            while current and ((count+1)<=_position):
                #found the position to insert into or reached last item
                # if last item, insert at the end
                if (count + 1 == _position) or (count + 1 == self._size):
                    self.node = self.Node(_value, current, current.next)
                    if current.next:
                        current.next.previous = self.node
                    current.next = self.node
                    self._size = self._size + 1
                    return self.node
                else:
                    current = current.next
                    count += 1
    def search(self, _value):
        if _value is None:
            raise ValueError('Cannot search for a value=None item to a list')
            
        current = self.head
        found = False
        while current and not found:
            if current.value == _value:
                found = True
            else:    
                current = current.next
        return current
        
    def delete(self, _value):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.value == _value:
                found = True
                self._size = self._size - 1
            else:
                previous = current
                current = current.next
        # nothing found, return None
        if not current:
            return None
        # the case where first item is being deleted
        if not previous:
            self.head = current.next
        # item from inside of the list is being deleted    
        elif current.next == None:
            previous.next = current.next
            self.tail = previous
        else: 
            previous.next = current.next
             
        return current

