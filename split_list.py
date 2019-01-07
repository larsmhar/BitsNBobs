def split_list(dict):
	dummy = {}
	for n in dict:
		index = 0
		dummy[n]= [[]]
		for i in dict[n]:
			print(dummy, n, dummy[n], index)
			if len(dummy[n][index]) > 3:
				index += 1
				dummy[n].append([])
			dummy[n][index].append(i)
	return dummy


dicti = split_list({"t": [1,2,3,4,5,6,7,8,9,10], "r": [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]})
print(split_list(dicti))
for n in dicti:
    print(n)
