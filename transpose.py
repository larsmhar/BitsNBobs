arr = [[1,2,3]]
arr2 = [[1,2,3],[4,5,6]]
arr3 = [[1,2,3],[4,5,6],[7,8,9]]

def transpose(xs):
	print(isinstance(xs, list))
	if isinstance(xs, list):
		return [[transpose(xs)] for i in range(len(xs[0]))]
	return xs

#print(transpose(arr))
#print(transpose(arr2))
def transpose2(input):
	return list(map(lambda *x: list(x), input))
	"""
	new_list = [[0 for i in range(len(arr2))] for y in range(len(arr2[0]))]
	for x in range(len(arr2)):
		for i in range(len(arr2[x])):
			new_list[i][x] = arr2[x][i]
	return new_list
	"""
print(transpose2(arr))
print(transpose2(arr2))
print(transpose2(arr3))

def transpose3(input):
    return list(map(lambda *row: list(row), *input))
print(transpose3(arr))
print(transpose3(arr2))
print(transpose3(arr3))
