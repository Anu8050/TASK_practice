class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
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
 
 
def first_common(llist1, llist2):
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
for data in data_list1:
    llist1.append(int(data))

data_list2 = [16,2,9,13,37,8,10,1,28,2]
for data in data_list2:
    llist2.append(int(data))

common = first_common(llist1, llist2)

if common:
    print('The two lists haveing common elements are {}.'.format(common))
else:
    print('The two lists have no common elements.')
    

for x in data_list2:
  data_list1.append(x)

print(data_list1)

print('After concatinating 2 list with out duplicate value' ,list(set(data_list1)))    
    
    
    
class Solution:
    def solve(self, L1, L2):
        if not L1:
            return L2
        if not L2:
            return L1
        
        
        # if L1.head < L2.head:
        #     res = L1
        #     res.next = self.solve(L1.next, L2)
        # elif L2 < L1:
        #     res = L2
        #     res.next = self.solve(L2.next, L1)
        # else:
        #     res = L1
        #     res.next = self.solve(L1.next, L2.next)
        return 
ob = Solution()
print(ob.solve(llist1, llist2))