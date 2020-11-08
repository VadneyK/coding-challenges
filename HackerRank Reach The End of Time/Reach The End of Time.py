import math 
import os 
import random 
import re 
import sys 
# # Complete the 'reachTheEnd' function below. # 
# # The function is expected to return a STRING. 
# # The function accepts following parameters: 
# #  1. STRING_ARRAY grid #  2. INTEGER maxTime 
# # 
def reachTheEnd(grid, maxTime): 

    visited = []
    for r in range(len(grid)):
        visited.append([])
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            visited[r].append(False)

    r, c = 0, 0
    queue = [] 
    path = []
    queue.append((r, c, 0))

    while queue: 
        pair = queue.pop() 
        r, c = pair[0], pair[1] 
        visited[r][c] = True

        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            path.append(pair[2])
            continue

        if r < len(grid) - 1: 
            if grid[r + 1][c] == '.' and not visited[r+1][c]: 
                queue.append((r+1, c, pair[2] + 1)) 

        if c < len(grid[0]) - 1: 
            if grid[r][c + 1] == '.' and not visited[r][c+1]: 
                queue.append((r, c+1, pair[2] + 1)) 

        if r > 0: 
            if grid[r - 1][c] == '.' and not visited[r-1][c]: 
                queue.append((r-1, c), pair[2] + 1) 

        if c > 0: 
            if grid[r][c - 1] == '.' and not visited[r][c-1]: 
                queue.append((r, c-1, pair[2] + 1)) 
    
    return min(path) <= maxTime

grid = ["..##", "#.##", "#..."]
maxTime = 5

print(reachTheEnd(grid, maxTime))