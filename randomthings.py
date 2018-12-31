arr = ["test", "testies", 1, "test"]

def is_in(array, element):
	return element in array


def print_odd(array):
	print(arr[0::2])


def count_in_array(array, element):
	return len(list(filter(lambda x: x == element, arr)))
	#return reduce((lambda: curr, total: if curr == element total = total + 1 else total), array)


print(count_in_array(arr, "test"))
print(print_odd(arr))
print(is_in(arr, "test"))
print(is_in(arr, "kittens"))
