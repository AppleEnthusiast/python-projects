numbers = {1,2,3,4,5,6,7}
print("original set:",numbers)

numbers.remove(2)
print("after remove(2):",numbers)

try:
	numbers.remove(99)
except KeyError as e:
	print("error ->",e)

numbers.discard(4)
print("after discard(4):",numbers)
numbers.discard(200)
print("after discard(200):",numbers)

num = numbers.pop()
print("after pop():",numbers)
print("number that has been removed with pop():",num)

numbers.clear()
print("after clear():",numbers)

