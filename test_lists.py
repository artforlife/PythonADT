import unittest
from lists import LinkedList, DLinkedList

class TestLinkedList(unittest.TestCase):
    linked_list=None
    def setUp(self):
        self.linked_list = LinkedList()
        
    def test_init(self):
        self.assertEqual(self.linked_list.head, None, "Initial HEAD should be None")
        self.assertEqual(len(self.linked_list), 0, "Initial length should be zero")
        
    def test_len(self):
        self.assertEqual(len(self.linked_list), 0, "Newly initiated list's length should be zero")
        self.linked_list.insert(1)
        self.assertEqual(len(self.linked_list), 1, "List length should be 1")        
    
    def test_list(self):
        node1 = self.linked_list.Node(1,None)
        node2 = self.linked_list.Node(2,node1)
        node3 = self.linked_list.Node(3,node2)
        self.linked_list.insert(1)
        self.linked_list.insert(2)
        self.linked_list.insert(3)
        self.assertEqual([node3,node2,node1], list(self.linked_list))
        
    def test_str(self):
        self.linked_list.insert(1)
        self.linked_list.insert(2)
        self.linked_list.insert(3)
        self.assertEqual(str(self.linked_list), '[3, 2, 1]', "List should be printed as [3, 2, 1]")
        self.linked_list.delete(2)
        self.assertEqual(str(self.linked_list), '[3, 1]',"List should be printed as [3, 1]")
        self.linked_list.delete(3)
        self.assertEqual(str(self.linked_list), '[1]', "List should be printed as [1]")
        self.linked_list.delete(1)
        self.assertEqual(str(self.linked_list), '[]', "List should be printed as []")
        
        
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
        
class TestDLinkedList(unittest.TestCase):
    d_linked_list = None
    
    def setUp(self):
        self.d_linked_list = DLinkedList()
        
    def test_init(self):
        self.assertEqual(self.d_linked_list.head, None, "Initial HEAD should be None")
        self.assertEqual(self.d_linked_list.tail, None, "Initial TAIL should be None")
        self.assertEqual(len(self.d_linked_list), 0, "Initial length should be zero")
        
    def test_insert_exceptions(self):
        self.assertRaises(ValueError, self.d_linked_list.insert, None, 0)
        self.assertRaises(ValueError, self.d_linked_list.insert, 1, -1)
    def test_search_exceptions(self):
        self.assertRaises(ValueError, self.d_linked_list.search, None)
        
    def test_list(self):
        node1 = self.d_linked_list.Node(1,None, None)
        node2 = self.d_linked_list.Node(2,node1, node3)
        node3 = self.d_linked_list.Node(3,node2)
        self.d_linked_list.insert(1)
        self.d_linked_list.insert(2)
        self.d_linked_list.insert(3)
        self.assertEqual([node3,node2,node1], list(self.d_linked_list))
        
    def test_contains(self):
        self.d_linked_list.insert(1,0)
        self.d_linked_list.insert(2,0)
        self.d_linked_list.insert(3,0)
        self.assertEqual(1 in self.d_linked_list, True, "After inserting 1 into the list, we should be able to find it there")
        self.assertEqual(4 in self.d_linked_list, False, "After inserting 1 into the list, we should be able to find it there")
        
    def test_insert_beginning(self):
        node1 = self.d_linked_list.insert(1,0)
        self.assertEqual(node1, self.d_linked_list.Node(1, None, None), "Inserting 1 into empty list should return node with value=1")
        self.assertEqual(self.d_linked_list.head, node1, "After inserting an element into the list, the HEAD != None")
        self.assertEqual(self.d_linked_list.tail, node1, "After inserting an element into the list, the TAIL != None")
        
        node2 = self.d_linked_list.insert(2,0)

        self.assertEqual(node2.value, self.d_linked_list.Node(2, None, None).value, "Inserting 2 into list at zeroth position should return the node itself")
        self.assertEqual(self.d_linked_list.head.value, node2.value, "After inserting second element into the list, the HEAD should point to that element")
        self.assertEqual(self.d_linked_list.tail.value, node1.value, "After inserting second element into the list, the TAIL should point to the first element inserted")
        self.assertEqual(self.d_linked_list.head.next.value, node1.value, "After inserting second element into the list, the first.next should point to the first inserted element")
        self.assertEqual(self.d_linked_list.tail.previous.value, node2.value, "After inserting second element into the list, the TAIL.previous should point to the newly inserted element")
        
        node3 = self.d_linked_list.insert(3,0)
        self.assertEqual(node3.value, self.d_linked_list.Node(3, None, None).value, "Inserting 3 into list at zeroth position should return the node itself")
        self.assertEqual(self.d_linked_list.head.value, node3.value, "After inserting second element into the list, the HEAD should point to that element")
        self.assertEqual(self.d_linked_list.tail.value, node1.value, "After inserting third element into the list, the TAIL should point to the first element inserted")
        self.assertEqual(self.d_linked_list.head.next.value, node2.value, "After inserting third element into the list, the first.next should point to the second inserted element")
        self.assertEqual(self.d_linked_list.tail.previous.value, node2.value, "After inserting third element into the list, the TAIL.previous should point to the secondly inserted element")
        
    def test_insert_position(self):
        self.assertEqual(str(self.d_linked_list), '[]', "List should be printed as [] when empty")
        node1 = self.d_linked_list.insert(1,0)
        self.assertEqual(node1, self.d_linked_list.Node(1, None, None), "Inserting 1 into empty list should return node with value=1")
        self.assertEqual(str(self.d_linked_list), '[1]', "List should be printed as [1] when node with value 1 is inserted")
        self.assertEqual(self.d_linked_list.head.value, node1.value, "After inserting first element into the list, the HEAD should point to the first element inserted")
        self.assertEqual(self.d_linked_list.tail.value, node1.value, "After inserting first element into the list, the TAIL should point to the first element inserted")
        node2 = self.d_linked_list.insert(2,0)
        self.assertEqual(self.d_linked_list.tail.value, node1.value, "After inserting second element into the list, the TAIL should point to the first element inserted")
        self.assertEqual(self.d_linked_list.head.value, node2.value, "After inserting second element into the list, the HEAD should point to the second element inserted")
        self.assertEqual(str(self.d_linked_list), '[2, 1]', "List should be printed as [2,1] when nodes with values 1 and 2 are inserted")
        node3 = self.d_linked_list.insert(3,1)
        self.assertEqual(str(self.d_linked_list), '[2, 3, 1]', "List should be printed as [2, 3, 1] when node with value 3 is inserted into position=1")
        node4 = self.d_linked_list.insert(4,3)
        self.assertEqual(str(self.d_linked_list), '[2, 3, 1, 4]', "List should be printed as [2, 3, 1, 4] when node with value 4 is inserted into position=3")
        
    def test_search(self):
       self.assertEqual(self.d_linked_list.search(1), None,'When searching an empty list for ANY item, the search should return None')
       node1 = self.d_linked_list.insert(1,0)
       self.assertEqual(self.d_linked_list.search(1), node1,'When searching the [1] list for 1, the search should return Node=1')
       node2 = self.d_linked_list.insert(2,0)
       self.assertEqual(self.d_linked_list.search(2).value, node2.value,'When searching the [2,1] list for 2, the search should return Node=2')
       node3 = self.d_linked_list.insert(3,1)
       self.assertEqual(self.d_linked_list.search(3).value, node3.value,'When searching the [2,3,1] list for 3, the search should return Node=3')
       node3 = self.d_linked_list.insert(4,3)
       self.assertEqual(self.d_linked_list.search(4).value, node3.value,'When searching the [2,3,1,4] list for 4, the search should return Node=4')
       
    def test_delete(self):
        self.assertEqual(self.d_linked_list.delete(1), None,'When trying to delete ANY item from empty list, the search should return None')
        node1 = self.d_linked_list.insert(1,0)
        self.assertEqual(self.d_linked_list.delete(1), node1,'When searching the [1] list for 1, the search should return Node=1')
        node2 = self.d_linked_list.insert(2,0)
        node3 = self.d_linked_list.insert(3,0)
        self.assertEqual(str(self.d_linked_list), '[3, 2]', "List should be printed as [3, 2] after node.value=3 is inserted into position=0")
        self.assertEqual(len(self.d_linked_list), 2, "List should be length=2 after inserting two elements")
        self.assertEqual(self.d_linked_list.delete(2), node2,'When deleting 1 from the list, the search should return Node=1')
        self.assertEqual(str(self.d_linked_list), '[3]', "List should be printed as [3] after node.value=2 is deleted")
#         print('self.head: ', self.d_linked_list.head.value)
#         print('self.tail: ', self.d_linked_list.tail.value)
        self.assertEqual(self.d_linked_list.tail.value, node3.value, "After deleting the 2 from [3,2] list, the TAIL should point to the [3] first element inserted")
        self.assertEqual(self.d_linked_list.head.value, node3.value, "After deleting the 2 from [3,2] list, the HEAD should point to the [3] first element inserted")
        node4 = self.d_linked_list.insert(4,0)
        self.assertEqual(str(self.d_linked_list), '[4, 3]', "List should be printed as [4, 3] after node.value=4 is inserted into position=0")
        self.assertEqual(self.d_linked_list.delete(3), node3,'When deleting 3 from the list, the search should return Node=3')
        self.assertEqual(self.d_linked_list.delete(4), node4,'When deleting 4 from the list, the search should return Node=4')
        self.assertEqual(str(self.d_linked_list), '[]', "List should be printed as [] all elements are deleted from it")
        
    def test_len(self):
        self.assertEqual(len(self.d_linked_list), 0, "Empty list is of length zero")
        node1 = self.d_linked_list.insert(1,0)
        self.assertEqual(len(self.d_linked_list), 1, "List with one element is of length=1")
        node2 = self.d_linked_list.insert(2,0)
        self.assertEqual(len(self.d_linked_list), 2, "List with two elements is of length=2")
        node3 = self.d_linked_list.insert(3,0)
        self.assertEqual(len(self.d_linked_list), 3, "List with three elements is of length=3")
        node4 = self.d_linked_list.insert(4,2)
        self.assertEqual(len(self.d_linked_list), 4, "List with four elements is of length=4")
        
    def test_list(self):
        self.assertEqual(str(self.d_linked_list), '[]', "List should be printed as [] when empty")
        node1 = self.d_linked_list.Node(1, None, None)
        self.d_linked_list.insert(1)
        self.assertEqual(str(self.d_linked_list), '[1]', "List should be printed as [1] after node.value=1 is inserted")
        node2 = self.d_linked_list.insert(2,0)
        self.assertEqual(str(self.d_linked_list), '[2, 1]', "List should be printed as [2, 1] after node.value=2 is inserted into position=0")
        node3 = self.d_linked_list.insert(3,1)
        self.assertEqual(str(self.d_linked_list), '[2, 3, 1]', "List should be printed as [2, 3, 1] after node.value=3 is inserted into position=1")
        node4 = self.d_linked_list.insert(4,3)
        self.assertEqual(str(self.d_linked_list), '[2, 3, 1, 4]', "List should be printed as [2, 3, 1, 4] after node.value=4 is inserted into position=3")
        node5 = self.d_linked_list.insert(5,10)
        self.assertEqual(str(self.d_linked_list), '[2, 3, 1, 4, 5]', "List should be printed as [2, 3, 1, 4, 5] after node.value=5 is inserted into position>length(list)")
        
    
if __name__ == '__main__':
    unittest.main()