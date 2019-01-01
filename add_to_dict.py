def add_to_dict(dict, dict_key, key, value):
	if dict_key in dict:
		if key in dict[dict_key]:
			dict[dict_key][key].append(value)
		else:
			dict[dict_key].update({key: [value]})
	else:
		dict[dict_key] = {key: [value]}


def add_to_dict2(dict, dict_key, value):
	if dict_key in dict:
		dict[dict_key].append(value)
	else:
		dict[dict_key] = [value]


dict = {}

add_to_dict(dict, "Por", "uri", "1")
print(dict)
add_to_dict(dict, "Maj", "uri", "33")
print(dict)
add_to_dict(dict, "Por", "uri", "2")
print(dict)
add_to_dict(dict, "Por", "genre", "prog")
print(dict)

print(3, dict)
