def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def count(lines):
	person = None
	count1 = 0
	count2 = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '柏維':
			for m in s[2:]:
				count1 += len(m)
		elif name == '林芳鈴（緣心、香香媽咪）':
			for m in s[2:]:
				count2 += len(m)
	print('柏維說了', count1, '個字')
	print('芳鈴說了', count2, '個字')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('line.txt')
	lines = count(lines)
	# write_file('output.txt', lines)

main()