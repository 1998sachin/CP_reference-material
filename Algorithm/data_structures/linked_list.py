class Node:
    def __init__(self,item):
        self.data=item
        self.next=None
import sys
class Unordered_list:
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=Node(item)
        temp.next=self.head
        self.head=temp
    def all(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def isEmpty(self):
        if self.head.next==None:
            return True
        else:
            return False
    def remove(self):
        if self.isEmpty():
            print("list is empty")
        else:
            temp=self.head
            self.head=self.head.next
            del temp

mylist=Unordered_list()
mylist.add(1)
mylist.add(12)
mylist.add(13)
mylist.add(14)
mylist.add(15)
# print(sys.getsizeof(mylist))
mylist.all()
print(mylist.isEmpty())
mylist.remove()
mylist.all()
# print(sys.getsizeof(mylist))
print(mylist.head.data,mylist.head.next.data,mylist.head.next.next.data)
print("sachin",34)
input("enter ")
