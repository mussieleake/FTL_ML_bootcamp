#Trasure Hunt Game


r = int(input("Enter number of rows:"))
c = int(input("Enter number of columns:"))
for i in range (r):
  for j in range (c):
    print("*",end="")
  print("*")
  
board = []  # Start with an empty board

for i in range(r):  # Iterate through rows
    row = []  # Create a new empty row
    for j in range(c):  # Iterate through columns
        row.append("*")  # Add an asterisk to the row
    board.append(row)  # Add the completed row to the board
r_hide = int(input("enter row number to hide the treasure:"))
c_hide = int(input("enter column number to hide the treasure:"))
if 0 <= r_hide < r and 0 <= c_hide < c:
  board[r_hide][c_hide] = "T"
for row in board:
  print("".join(row))
