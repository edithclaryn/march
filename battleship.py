"""Create a 5 x 5 grid initialized to all 'O's and store it in board.

Use range() to loop 5 times.
Inside the loop, .append() a list containing 5 "O"s to board.
Note that these are capital letter "O" and not zeros."""
board = []
for i in range(0,5):
	board.append(["O"]*5)
print (board)
#Use the print command to display the contents of the board list.


"""First, delete your existing print statement.
Then, define a function named print_board with a single argument, board.
Inside the function, write a for loop to iterates through each row in board and print it to the screen.
Call your function with board to make sure it works."""
def print_board(board):
	for i in board:
		print (i)
print_board(board)

"""to remove commas in the list:
 Inside your function, inside your for loop, use " " as the separator to .join the elements of each row."""
def print_board(board):
    for row in board:
        print (" ".join(row))
print_board(board)