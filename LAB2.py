n = int(input("Enter number of rows :"))
m = int(input("Enter number of columns :"))

grid = []
print("Enter the grid :")
for i in range (n):
    grid.append(input().split())

row = 0
col = 0 
visited = []

while True:
    visited.append((row,col))
    print("Current Position",(row,col))

    if(grid[row][col] == 'G'):
        print("Goal is reached")
        break

    if( col <col-1 and grid[row][col+1] != 'X' and (row,col+1) not in visited):
        col = col +1

    elif(row < row-1 and grid[row+1][col] != 'X' and (row+1,col) not in visited):
        row = row +1
    
    elif(row > 0 and grid[row-1][col] != 'X' and (row-1,col) not in visited):
        row = row -1

    elif(col > 0 and grid[row-1][col] != 'X' and (row,col-1) not in visited ):
        col = col -1

    else :
        print("No path found")
        break 
    

print("visited cells :", visited)