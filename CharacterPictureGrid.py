# Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(6):
    for y in range(9):
        print(grid[y][x],end='')
    print('')

grid1 = [['a','b','c'],
        [1,2,3],    	
        ['x','y','z']]

print(grid1[0][0])
print(grid1[1][0])
print(grid1[2][0])
print(grid1[0][1])
print(grid1[1][1])
print(grid1[2][1])
print(grid1[0][2])
print(grid1[1][2])
print(grid1[2][2])
