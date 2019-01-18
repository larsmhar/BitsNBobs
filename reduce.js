let arr = [1,3,5,1,5,7,1,2,4,6,8,5,1,3,45,6,7]

console.log(arr.reduce((acc, x) => {
	acc[x] ? acc[x] += 1 : acc[x] = 1
	return acc
}, {}))
