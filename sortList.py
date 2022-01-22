# Create a SIMPLY LINKED LIST
# Which is ALWAYS IN ORDER (lowest to highest)

# I am providing 3 dunder methods:
#  - an initializer that may be helpful, but you are welcome to change it if the autograder still works.
#  - an string method, to print the list
#  - a representer method, to show the list at command line

# With the following public methods:
#  - insert: given input data, returns as output the list with that data added
#  - insert: given input data, returns as output the list with that data no longer present
#  - contains: given input data, returns True if the data is in the list, False otherwise
#  - size: given no inputs, return a integer giving the size of the list
#  - index: given an input integer i, return the ith smallest element of the list, starting from zero or None of if the index is too ldatae

# Use None to denote a list with no elements

class SortList:
	def __repr__(self):
		''' Provided '''
		if self.rest != None:
			return "(" + str(self.data) + ")->" + self.rest.__repr__()
		else:
			return "(" + str(self.data) + ")"
	def __str__(self):
		''' Provided '''
		return self.__repr__()
	
	# INITIALIZER / CONSTRUCTOR
	# Two inputs: data to be contained in the list
	#             optional: a list containing the other elements of the list (the rest of the list)
	# One output: the new list containing that data and the provided list
	# ex:
	# >>> some_list = SortList(5)
	# >>> some_list
	# (5)
	# >>> some_other_list = SortList(4,some_list)
	# >>> some_other_list
	# (4)->(5)
	# >>> a_third_list = SortList(3,some_other_list)
	# >>> a_third_list
	# (3)->(4)->(5)
	def __init__(self, data, rest = None):
		''' Provided '''
		self.data = data
		self.rest = rest
	
	# INSERT
	# One input: data to be contained in the list
	# One output: the new list containing that data in the appropriate location
	# ex:
	# >>> some_list
	# (2)->(4)
	# >>> some_list = some_list.insert(1)
	# >>> some_list
	# (1)->(2)->(4)
	# >>> some_list = some_list.insert(1)
	# >>> some_list
	def insert(self, data):
		''' TODO: Return the list with data in the correct order (if data is natural) '''
		pass
	
	# REMOVE
	# One input: data to be removed from the list
	# One output: the new list with the data removed
	# ex:
	# >>> some_list
	# (1)->(2)->(4)
	# >>> some_list = some_list.remove(1)
	# >>> some_list
	# (2)->(4)
	# >>> some_list = some_list.remove(4)
	# >>> some_list
	# (2)
	# >>> some_list = some_list.remove(2)
	# >>> some_list
	# None
	def remove(self, data):
		pass
		
	# CONTAINS
	# One input: data to be checked for presence in list
	# One output: either True if the data is present and False otherwise
	# ex:
	# >>> some_list
	# (1)->(2)->(4)
	# >>> some_list.contains(2)
	# True
	# >>> some_list.contains(3)
	# False
	def contains(self, data):
		pass
	
	# SIZE
	# No inputs
	# One output: and integer giving the number of elements in the list
	# ex:
	# >>> some_list
	# (1)->(2)->(4)
	# >>> some_list.size()
	# 3
	# >>> SortList(5).size()
	# 1
	def size(self):
		pass
	
	# Index
	# One input: an integer i
	# One output: the ith element of the list if present, or None
	# ex:
	# >>> some_list
	# ("a")->("b")->("c")
	# >>> some_list.index(0)
	# "a"
	# >>> some_list.index(3)
	# None
	def index(self, i):
		pass