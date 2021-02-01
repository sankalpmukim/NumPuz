from random import randint

def numToString(n):
	if(n<10):
		return '0'+str(n)
	else:
		return str(n)

def boardDisplayer(board):
	print('|  ',end = '')
	print('# '*int(len(board)*(3/2))+ (' ' if len(board)%2 else ''), end = ' |\n')
	for i in board: #board is a list of lists.
		print('| ', end = ' ')
		for j in i:
			print(j, end = ' ')
		print(' |')
	print('|  ',end = '')
	print('# '*int(len(board)*(3/2)), end = ' |\n')

def idealBoard(n):
	idealBoard = [[] for i in range(n)]
	for i in range(n):
		for j in range(n):
			idealBoard[i].append(numToString(i*n+j+1))
	idealBoard[n-1][n-1] = '  '
	return idealBoard

def findIJ(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if(board[i][j]=='  '):
				return i,j

def up(board):
	i,j = findIJ(board)
	board[i-1][j], board[i][j] = board[i][j], board[i-1][j]

def down(board):
	i,j = findIJ(board)
	board[i+1][j], board[i][j] = board[i][j], board[i+1][j]

def left(board):
	i,j = findIJ(board)
	board[i][j-1], board[i][j] = board[i][j], board[i][j-1]

def right(board):
	i,j = findIJ(board)
	board[i][j+1], board[i][j] = board[i][j], board[i][j+1]

def main(n):
	#n used to create an nxn board
	N=n**2
	values = list()
	while(len(values)<N): # used to create an random order of values from 0 to N-1
		temp = randint(1,N)
		if temp not in values:
			values.append(temp)
	print(values)
	board=[[] for i in range(n)]
	for i in range(n):
		for j in range(n):
			board[i].append(numToString(values[i*n+j]))
			if(board[i][j]==numToString(n**2)):
				board[i][j]='  '
	
	correctBoard = idealBoard(n)
	boardDisplayer(correctBoard)
	print()
	boardDisplayer(board)
	# Till this point, 
	# I have a randomly generated board,
	# An Ideal board to compare win/loss with
	# Now, I just need up,down,left,right commands to make a functioning game
	print("GAME DATA SUCCESFULLY GENERATED")
	while True:
		print(f"Type w,a,s,d for moving the ## value to arrange the values in order.")
		moves = input()
		for move in moves:
			i,j = findIJ(board)
			if(move == 'w'):
				if(i<=0):
					print("Top Edge Error")
				else:
					up(board)
			elif(move == 's'):
				if(i>=n-1):
					print("Bottom Edge Error")
				else:
					down(board)
			elif(move == 'a'):
				if(j<=0):
					print("Left Edge Error")
				else:
					left(board)
			elif(move == 'd'):
				if(j>=n-1):
					print("Right Edge Error")
				else:
					right(board)
			else:
				print("Invalid input error")
			
		boardDisplayer(board)
		if(board == correctBoard):
			break
	print("GAME OVER!\nYOUU WON!!")

if __name__ == '__main__':
	main(4)