import subprocess as sp
lst = ["","X"," "," "," "," "," "," "," "," "]
def board():
	print('Current board')
	print("1 | 2 | 3     "+lst[1]+" | "+lst[2]+" | "+lst[3])
	print("---------     ---------")
	print("4 | 5 | 6     "+lst[4]+" | "+lst[5]+" | "+lst[6])
	print("---------     ---------")
	print("7 | 8 | 9     "+lst[7]+" | "+lst[8]+" | "+lst[9]+"\n")
def win():
	flag = 0
	for i in range(1,8,3):
		if lst[i]==lst[i+1]==lst[i+2]=='X':
			print('---YOU LOST---')
			flag = 1
		elif lst[i]==lst[i+1]==lst[i+2]=='O':
			print('---YOU WON---')
			flag = 1
	if flag == 0:
		for i in range(1,4):
			if lst[i]==lst[i+3]==lst[i+6]=='X':
				print('---YOU LOST---')
				flag = 1
			elif lst[i]==lst[i+3]==lst[i+6]=='O':
				print('---YOU WON---')
				flag = 1
	if flag == 0:
		if lst[1]==lst[5]==lst[9]=='X' or lst[3]==lst[5]==lst[7]=='X':
			print('---YOU LOST---')
			flag = 1
		elif lst[1]==lst[5]==lst[9]=='X' or lst[3]==lst[5]==lst[7]=='O':
			print('---YOU WON---')
			flag = 1
	if flag == 1:
		return True
	else:
		return False
for i in range(1,10):
	if i == 9:
		print('---TIE---')
		board()
		break
	if i%2 == 1:
		board()
		inp = int(input('Enter position:'))
		if inp > 1 and inp < 10 and lst[inp] == ' ':
			lst[inp] = 'O'
		else:
			while True:
				inp = int(input('INCORRECT!!! Enter position again:'))
				if inp > 1 and inp < 10 and lst[inp] == ' ':
					lst[inp] = 'O'
					break
		if win():
			board()
			break
		sp.call('cls',shell=True)
	if i == 2:
		if lst[2] == 'O':
			lst[5] = 'X'
		elif lst[3] != 'O':
			lst[3] = 'X'
		elif lst[9] != 'O':
			lst[9] = 'X'
	elif i == 4:
		if lst[3] == 'X' and lst[2] != 'O':
			lst[2] = 'X'
		elif lst[3] == 'X' and lst[2] == 'O' and lst[7] != 'O' and lst[5] != 'O' and lst[9] != 'O':
			lst[5] = 'X'
		elif lst[3] == 'X' and lst[2] == 'O' and lst[7] == 'O':
			lst[9] = 'X'
		elif lst[3] == 'X' and lst[2] == 'O' and lst[9] == 'O':
			lst[7] = 'X'
		elif lst[9] == 'X' and lst[5] != 'O':
			lst[5] = 'X'
		elif lst[9] == 'X' and lst[5] == 'O':
			lst[7] = 'X'
		elif lst[5] == 'X' and lst[9] != 'O':
			lst[9] = 'X'
		elif lst[5] == 'X' and lst[9] == 'O':
			lst[7] = 'X'
		elif lst[5] == 'O' and lst[2] != 'O':
			lst[2] = 'X'
		elif lst[5] == 'O' and lst[2] == 'O':
			lst[8] = 'X'
	elif i == 6:
		if lst[3] == 'X' and lst[2] == 'O' and lst[5] == 'X':
			if lst[9] != 'O':
				lst[9] = 'X'
			else:
				lst[7] = 'X'
		elif lst[3] == 'X' and lst[2] == 'O' and lst[7] == 'O' and lst[9] == 'X':
			if lst[5] != 'O':
				lst[5] = 'X'
			else:
				lst[6] = 'X'
		elif lst[9] == 'X' and lst[5] == 'O' and lst[7] == 'X':
			if lst[4] != 'O':
				lst[4] = 'X'
			else:
				lst[8] = 'X'
		elif lst[5] == 'X' and lst[9] == 'O' and lst[7] == 'X':
			if lst[4] != 'O':
				lst[4] = 'X'
			else:
				lst[3] = 'X'
		elif lst[3] == 'X' and lst[9] == 'O' and lst[7] == 'X':
			if lst[4] != 'O':
				lst[4] = 'X'
			else:
				lst[5] = 'X'
		elif lst[5] == 'O' and lst[2] == 'O' and lst[8] == 'X':
			if lst[4] == 'O':
				lst[6] = 'X'
			elif lst[6] == 'O':
				lst[4] = 'X'
			elif lst[7] == 'O':
				lst[6] = 'X'
			else:
				lst[4] = 'X'
	elif i == 8:
		for i in range(2,10):
			if lst[i] != 'O' and lst[i] != 'X':
				lst[i] = 'X'
	if win():
		board()
		break