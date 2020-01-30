def SplitNumber(Input):
	return SplitStrNumber(str(Input))

def SplitStrNumber(Input):
	Number = Input
	if len(Number) == 0:
		return None
	i = len(Number) - 1
	while i > 0:
		if Number[i] == '.':
			break
		i -= 1
	if i == 0 and Number[0] == '.':
		return Number
	if Number[i] == '.':
		i = i - 3
	else:
		i = len(Number) - 3
	while i > 0:
		Number = Number[:i] + " " + Number[i:]
		i -= 3
	return Number
