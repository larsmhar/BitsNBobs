def mountain(levels):
	def inner(level, space):
		if level == 0:
			return ""
		return (" " * level) + "/" + (" " * space) + "\\\n" + inner(level - 1, space + 2)
	return inner(levels, 0)

print(mountain(5))
