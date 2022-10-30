a = [[1, 6, 8, 5, 4, 0, 3],
     [5, 7, 8, 9, 4, 2, 1],
     [6, 0, 7, 8, 1, 2, 5],
     [5, 7, 2, 7, 5, 2, 1],
     ]

k = -1
for i in a:
    k += 1
    g = (a[k])
    for i in range(1):
        print(g[len(g) - len(g)], g[len(g) - 1])

print(" ")

matrix = [[1, 6, 8, 5, 4, 0, 3],
          [5, 7, 8, 9, 4, 2, 1],
          [6, 0, 7, 8, 1, 2, 5],
          [5, 7, 2, 7, 5, 2, 1],
     ]


for i, value_1 in enumerate(matrix):
    print(*[matrix[i][j] for j, value_2 in enumerate(value_1) if j % 2 == 0 and matrix[0][j] > matrix[len(matrix)-1][j]])


board = [
    ['x', 'x', 'o'],
    ['o', 'x', 'o'],
    ['o', 'o', 'x'],
]

winner = None

for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
        winner = board[i][0]
    if board[0][i] == board[1][i] == board[2][i]:
        winner = board[0][i]
if board[0][0] == board[1][1] == board[2][2]:
    winner = board[0][0]
if board[0][2] == board[1][1] == board[2][0]:
    winner = board[0][2]

if winner:
    print(f'Winner is {winner}')
else:
    print('Draw')