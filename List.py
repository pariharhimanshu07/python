'''List is one of the commonly used data structure in Python for storing the data.
The following operations we are going to cover using List
1.append
2.count
3.extend
4.index
5.insert
6.pop
7.remove
8.reverse
9.sort
'''

#1
'''In the first operation here we are going to append item to our existing list (dummy_list)'''
import time
from datetime import datetime
startTime = datetime.now()
def list_append():
	dummy_list=[1,2,3,4]
	item=5
	dummy_list.append(item)
	return dummy_list
print list_append()

#The output for the following would [1, 2, 3, 4, 5] .The change we can notice is that 5 is being added to the existing list.

#2
'''The second operation we are going to perform is "count". It is used to get the count of elements in a list.'''
def list_count():
	dummy_list=[1,1,2,3,4,5]
	#Now suppose we want to check the count of element 1 in the list. So we can do that by following.
	return dummy_list.count(1)
print list_count()

#Here the output will be 2 . As the count of 1 in dummy_list is 2.

#3
'''The third operation we are going to cover is 'extend'. Suppose we have two list and we want the second list to continue over the firt
then we will be using extend'''
def list_extend():
	dummy_list1=[1,2,3,4,5]
	dummy_list2=[6,7,8]
	#Now we want to club the dummy_list1 and dummy_list2. Then using extend function we can achieve that.
	dummy_list1.extend(dummy_list2)
	#Here the dummy_list2 follows the dummy_list1.
	return dummy_list1
print list_extend()
#Here the output will be [1, 2, 3, 4, 5, 6, 7, 8]. So we can notice that dummy_list2 just follows dummy_list1 and we can get the combined output in dummy_lis1.

#4
'''The fourth operation we are going to cover is "index". It is used to get the index/position of our element we want to search in the list'''
def list_index():
	dummy_list=range(100,190)
	check_item=178
	#dummy_list will return us a list that starts from 100 and ends at 189. Now what if we want to check the index of 178 in the list?
	#In that case we can use the index.
	return dummy_list.index(check_item)
print list_index()

#Here the output would be 78 that is the position of 178 in dummy_list.

#5
'''The fifth item we are going to cover is "insert". As the name implies it is used to insert an element in the list.
But we are able to add an element using "append" also.
So the key benefit of "insert" is that it is used to insert at an specific position.
Suppose we want to insert at position 17 in a list and we want that other elements in list should auto adjust. 
Then we use "insert". '''

def list_insert():
	dummy_list=range(20,40)
	item_insert=121
	#Here we will be inserting item_insert into 17th position in dummy_list.
	dummy_list.insert(17,item_insert)
	return dummy_list
print list_insert()

#Here the output would be [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 121, 37, 38, 39].
#We can see that in position 17 we have 121.

#6
'''The sixth operation we are going to cover is pop. It is used to remove an element from the list at the specified position.
If the position is not specified by default it will remove the last element.
'''

def list_pop():
	dummy_list=range(70,80)
	#Now suppose we want to remove the element at 7th position. We can achieve that using pop.
	position=7
	dummy_list.pop(position)
	return dummy_list
print list_pop()

#Here the output is [70, 71, 72, 73, 74, 75, 76, 78, 79].
#So we can see that the element is 7th position that is 77 is removed.

#7
'''The seventh operation we are going to cover is "remove". It is used to remove an specific element from the list.
Suppose we have a list and we want to remove an element from the list. We can use "remove".
But we were able to remove using "pop" also. So why are we moving to remove ?
We can use pop only when we know the position of element we want to remove.
But in the case of remove we just need to know the element we want to remove '''

def list_remove():
	dummy_list=range(200,220)
	item_remove=219
	dummy_list.remove(item_remove)
	return dummy_list
print list_remove()

#Here the output would be [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218].
#We can see that 219 is being removed from the list.

#8 
'''The eight operation we are going to cover is "reverse".It is used to reverse the order of a list'''
def list_reverse():
	dummy_list=range(0,10)
	dummy_list.reverse()
	return dummy_list
print list_reverse()
#Here the output would be [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#We can see that the order is reversed completely.

#9
'''The 9th operation we are going to cover is "sort".It is used to sort a given list'''
def list_sort():
	dummy_list=[0,2,5,1,3,6,7,8,9,4]
	dummy_list.sort()
	return dummy_list
print list_sort()
end=datetime.now()
print startTime-end
#Here the output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#So we can see that the output list is in sorted manner.