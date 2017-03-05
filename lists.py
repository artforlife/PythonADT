class LinkedList(object):
    class Node(object):
        """
        Inner class of LinkedList. Contains a blueprint for a node of the LinkedList
        """
        def __init__(self, value, next=None):
            """
            Initializes a List node with payload v and link n
            """
            self.value=value
            self.next=next
        
        def __eq__(self,other):
            """
            Defining comparison between nodes for unit testing
            """
            if self.value == other.value and self.next == other.next:
                return True
            else:
                return False
            
         
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
                found = True
                return True
            else:
                current = current.next
        if not current:
            return False 
        
    def __bool__(self):
        """
        Implements boolean check of the class
        """
        if self.__len__() == 0:
            return False
        else:
            return True
                
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
        else:
            current = self.__current
            self.__current=self.__current.next
            return current
            
    def __str__(self):
        """
        Prints the current list in the form of a Python list            
        """
        current = self.head
        toPrint = []
        while current:
            toPrint.append(current.value)
            current = current.next
        return str(toPrint)      
         
    def insert(self, value, position=0):
        """
        Adds an item with payload v to beginning of the list
        in O(1) time or to position in the list in O(n) time 
        """
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
    class Node(object):
        """
        Inner class of LinkedList. Contains a blueprint for a node of the LinkedList
        """
        def __init__(self, v, p=None, n=None):
            """
            Initializes a List node with payload v, previous link p, next link n
            """
            self.value=v
            self.next=n
            self.previous=p
            self.size=0
    
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __str__(self):
        current = self.head
        toPrint = []
        while current != None:
            toPrint.append(current.value)
            current = current.next
        return str(toPrint)
        
    def addHead(self,v):
        # if adding the first node, we must
        # set the head and tail of the list to 
        # this node
        if not self.tail and not self.head:
            Node = self.Node(v, None, None)
            self.head = Node
            self.tail = Node
        # there are already nodes in the list and
        # the new one is simply added to the beginning    
        else:
            Node = self.Node(v, None, self.head)
            self.head.previous = Node
            self.head = Node
        
    def addTail(self,v):
        if not self.tail and not self.head:
            Node = self.Node(v, None, None)
            self.head = Node
            self.tail = Node
        # there are already nodes in the list and
        # the new one is simply added to the beginning    
        else:
            Node = self.Node(v, self.tail, None)
            self.tail.next = Node
            self.tail = Node 
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
        
    def search(self, v):
        current = self.head
        found = False
        while current and not found:
            if current.value == v:
                found = True
            else:
                current = current.next
        if not current:
            return None
        return current
        
    def delete(self, v):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.value == v:
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
        elif not next:
            self.tail = current.previous   
        else:
            previous.next = current.next
             
        return current      
             
        
        
