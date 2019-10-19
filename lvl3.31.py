# Prepare the Bunnies' Escape

def shortest_path(sx, sy, maze):
    width = len(maze[0])
    height = len(maze)
    board = [[None for i in range(width)] for i in range(height)]
    board[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < height and 0 <= ny < width:
                if board[nx][ny] is None:
                    board[nx][ny] = board[x][y] + 1
                    if maze[nx][ny] == 1:
                        continue
                    arr.append((nx, ny))

    return board


def solution(maze):
    width = len(maze[0])
    height = len(maze)
    top2Bot = shortest_path(0, 0, maze)
    bot2Top = shortest_path(height - 1, width - 1, maze)

    ans = 2 ** 32 - 1
    for i in range(height):
        for j in range(width):
            if top2Bot[i][j] and bot2Top[i][j]:
                ans = min(top2Bot[i][j] + bot2Top[i][j] - 1, ans)
    return ans


# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]

print(solution(maze))
