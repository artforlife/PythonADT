class LinkedList(object):
    class Node(object):
        def __init__(self, v, n=None):
            """
            Initializes a List node with payload v and link n
            """
            self.value=v
            self.next=n
         
    def __init__(self):
        """
        Initializes a LinkedList and sets list head to None
        """
        self.head=None
         
    def push(self, v):
        """
        Adds an item with payload v to beginning of the list
        in O(1) time 
        """
        Node = self.Node(v, self.head)
        self.head = Node
        print("Added item: ", Node.value, "self.head: ", self.head.value)
         
    def size(self):
        """
        Returns the current size of the list. O(n), linear time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
         
    def __str__(self):
        """
        Prints the current list in the form of a Python list            
        """
        current = self.head
        toPrint = []
        while current != None:
            toPrint.append(current.value)
            current = current.next
        return str(toPrint)
