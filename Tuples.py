'''Tuple is a sequence of values much like a list. 
The values stored in a tuple can be any type, and they are indexed by integers. 
The important difference is that tuples are immutable. 
Tuples are also comparable and hashable so we can sort lists of them and use tuples as key values in Python dictionaries.
Syntactically, a tuple is a comma-separated list of values
Tuples are enclosed by paranthesis

To create a tuple with a single element, you have to include the final comma:

 
>>> t1 = ('a',)
>>> type(t1)
<type 'tuple'>
Without the comma Python treats ('a') as an expression with a string in parentheses that evaluates to a string:

>>> t2 = ('a')
>>> type(t2)
<type 'str'>
'''

#Operation 1 :- count
#Using the count function in tuple we can get the count of a specific element in a tuple.
def tuple_count():
	items=0,1,2,1,2,1,4,5,6,3
	#Now we will be creating a tuple tuple_final with all the elements of items.
	tuple_final=tuple(items)
	count_item=1
	#Here suppose we want to count the number of times 1 is in the tuple.Then using count function we can achieve that.
	return tuple_final.count(count_item)
print tuple_count()
#Here the output would be 2. As the number of times 1 appears in the tupple is 3.

#Operation 2 :- index
#Using the index function in tuple we can get to know the position of a element in a tuple.

def tuple_index():
	items=0,1,2,1,2,1,4,5,6,3
	#Now we will be creating a tuple tuple_final with all the elements of items.
	tuple_final=tuple(items)
	item_index=5
	return tuple_final.index(item_index)
print tuple_index()
#Here the output would be 7. As the indez of 5 in the tuple is 7th .