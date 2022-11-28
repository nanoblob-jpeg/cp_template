def call(filename, templates):
	functions = dict()
	funcs = open("C:/Users/jerry/bin/staticTemplate/alias.txt", "r")
	for line in funcs:
		x, y = line.split()
		x = x.strip()
		y = y.strip()
		functions[x] = y
	funcs.close()

	file = open(filename, "r")
	lines = file.readlines()
	file.close()
	index = 0
	while lines[index].strip() != '//! function insert':
		index += 1
	for name in templates:
		if name == "list":
			print(*[n for n in sorted(functions.keys())], sep = '\n')
			continue
		if name not in functions:
			continue
		toWriteFile = open(functions[name], "r")
		for line in toWriteFile:
			if line[-1] == '\n':
				lines.insert(index, line)
			else:
				lines.insert(index, line+'\n')
			index += 1
		toWriteFile.close()

	file = open(filename, "w")
	for line in lines:
		file.write(line)
	file.close()