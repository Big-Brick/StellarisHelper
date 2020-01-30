def dict_to_table(data):
	text = str()
	first = True
	for key, value in data.items():
		if not first:
			string = "\n" + str(key) + " - " + str(value)
		else:
			string = str(key) + " - " + str(value)
			first = False
		text += string
	return text
