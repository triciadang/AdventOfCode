from collections import deque
from typing import List, Tuple

# Movement directions (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(
	row: int, col: int, grid: List[str], visited: List[List[bool]]
) -> Tuple[int, int]:
	# Shorthand for the size of the grid
	n = len(grid)

	queue = deque()
	queue.append((row, col))  # Start BFS from the given cell (row, col)

	area = 0
	perimeter = 0

	while queue:
		row, col = queue.popleft()  # Current cell (row, col)

		# Skip if the cell has already been visited
		if visited[row][col]:
			continue

		visited[row][col] = True  # Mark the cell (row, col) as visited
		area += 1  # Increment area (each '#' contributes 1 to the area)

		# Each cell starts with 4 sides contributing to the perimeter
		sides = 4
		for dx, dy in DIRECTIONS:
			next_row = row + dx
			next_col = col + dy

			# Check if the neighboring cell is within the grid
			if 0 <= next_row < n and 0 <= next_col < n:
				# If the neighbor (next_row, next_col) is part of the same blob
				if grid[next_row][next_col] == "A":
					# Add the neighbor (next_row, next_col) to the queue
					queue.append((next_row, next_col))
					sides -= 1  # Shared edges reduce the perimeter contribution

		perimeter += sides  # Add remaining sides to the perimeter

	return area, perimeter


with open("input.txt", "r") as fin:
	n = int(fin.readline().strip())
	grid = [fin.readline().strip() for _ in range(n)]

visited = [[False] * n for _ in range(n)]

max_area = 0
min_perimeter = -99999999999
for i in range(n):
	for j in range(n):
		if grid[i][j] != "A" or visited[i][j]:
			continue

		area, perimeter = bfs(i, j, grid, visited)

		# Update max_area and min_perimeter based on the BFS results
		if area > max_area or (area == max_area and perimeter < min_perimeter):
			max_area = area
			min_perimeter = perimeter

print(f"{max_area} {min_perimeter}")