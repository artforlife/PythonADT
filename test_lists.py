import unittest
from lists import LinkedList

class TestLinkedList(unittest.TestCase):
    linked_list=None
    def setUp(self):
        self.linked_list = LinkedList()
        
    def test_init(self):
        self.assertEqual(self.linked_list.head, None, "Initial HEAD should be None")
        self.assertEqual(len(self.linked_list), 0, "Initial length should be zero")
        
    def test_insert(self):
        self.assertEqual(self.linked_list.insert(1), self.linked_list.Node(1, None), "Inserting 1 into list should return node with value=1")
        self.assertEqual(list(self.linked_list),[self.linked_list.Node(1)], "Inserting 1 into empty list should give [1]")
        self.linked_list.insert(3,1)
        self.assertEqual(self.linked_list.head.next, self.linked_list.Node(3, None), "Inserting 3 into pos=1 of [1] should give [1,3]")
        self.linked_list.insert(2,1)
        self.assertEqual(self.linked_list.head.next.value, self.linked_list.Node(2, None).value, "Inserting 2 into pos=1 of [1,3] should give [1,2,3]")
        
    def test_contains(self):
        self.linked_list.insert(1)
        self.linked_list.insert(2)
        self.linked_list.insert(3)
        self.assertEqual(1 in self.linked_list, True, "After inserting 1 into the list, we should be able to find it there")
        self.assertEqual(4 in self.linked_list, False, "After inserting 1 into the list, we should be able to find it there")
        #print(self.linked_list)
        
    def test_search(self):
        self.linked_list.insert(1)
        self.linked_list.insert(2)
        self.linked_list.insert(3)
        self.assertEqual(self.linked_list.search(2).value, self.linked_list.Node(2, None).value, "Searching for 2 in [3,2,1] should return node with value=2")
        self.assertEqual(self.linked_list.search(4), None, "Searching for 4 in [3,2,1] should return None")
        
    def test_delete(self):
        self.linked_list.insert(1)
        self.linked_list.insert(2)
        self.linked_list.insert(3)
        self.assertEqual(self.linked_list.delete(2).value, self.linked_list.Node(2, None).value, "Deleting 2 from [3,2,1] should return the node with value 2")
        self.linked_list.delete(3)
        self.assertEqual(self.linked_list.head, self.linked_list.Node(1, None), "Deleting 2 and 3 from [3,2,1] should leave the list as [1]")
        
    
    
if __name__ == '__main__':
    unittest.main()