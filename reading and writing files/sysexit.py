import sys
while True:
	print('Type exit to exit.')
	response = input()
	if response == 'exit':
		sys.exit()
	else:
		print('You typed ' + response + '.')
		continue
