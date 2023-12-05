def bfs(grid, *start):
    Q = [(x, y, 0, 'a') for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] in start]
    visited = set((i, j) for i, j, _, _ in Q)

    while Q:
        x, y, d, a = Q.pop(0)
        if grid[x][y] == 'E':
            return d

        for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if not 0 <= nx < len(grid) or not 0 <= ny < len(grid[nx]) or (nx, ny) in visited:
                continue
            b = grid[nx][ny].replace('E', 'z')
            if ord(b) > ord(a) + 1:
                continue
            visited.add((nx, ny))
            Q.append((nx, ny, d + 1, b))


file = open("input").readlines()
print(bfs(file, 'S'), bfs(file, 'S', 'a'))
