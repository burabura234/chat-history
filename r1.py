# 改變對話格式

#讀取檔案

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#變換格式

def convert(lines):
	new = []
	name = None
	for line in lines:
		if line == 'Allen':
			name = 'Allen'
			continue
		elif line == 'Tom':
			name = 'Tom'
			continue
		if name:
			new.append(name + ': ' + line)
	return new

# 寫入output

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')
		

#主程式
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

#主程式執行
main()