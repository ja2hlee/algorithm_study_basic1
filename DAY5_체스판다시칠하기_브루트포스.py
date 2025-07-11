def count_repaint(board, x, y):
    draw1, draw2 = 0, 0  #B로 시작, W로 시작

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == 0:
                if board[i][j] != 'B':
                    draw1 += 1
                if board[i][j] != 'W':
                    draw2 += 1
            else:
                if board[i][j] != 'W':
                    draw1 += 1
                if board[i][j] != 'B':
                    draw2 += 1

    return min(draw1, draw2)


n, m = map(int, input().split())
board = [input() for _ in range(n)]

result = []
for i in range(n - 7):
    for j in range(m - 7):
        result.append(count_repaint(board, i, j))

print(min(result))


# In[ ]:




