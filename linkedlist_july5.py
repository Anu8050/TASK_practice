class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
#this class is for creating a linked list
class Linkedlist:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
# Elements that are common in linkedlist llist1 and llist2.
def common_element(llist1, llist2):
    current1 = llist1.head
    while current1:
        data = current1.data
        current2 = llist2.head
        while current2:
            if data == current2.data:
                return data
            current2 = current2.next
        current1 = current1.next
    return None

llist1 = Linkedlist()
llist2 = Linkedlist()


data_list1 = [3,7,10,15,16,9,22,17,32,3]
#Inserting element to a first linked list. 
for data in data_list1:
    llist1.append(int(data))

data_list2 = [16,2,9,13,37,8,10,1,28,2]
#Inserting element to a second linked list.
for data in data_list2:
    llist2.append(int(data))

#Calling function by passing parameter 
common = common_element(llist1, llist2)

if common:
    print('The two lists haveing common elements are {}.'.format(common))
else:
    print('The two lists have no common elements.')
    
#contains all elements of l1 as well as l2 ensuring that there is no repeation of elements.
for x in data_list2:
  data_list1.append(x)

print(data_list1)

print('After concatinating 2 list with out duplicate value' ,list(set(data_list1)))    
    
    
