from collections import deque

# Movement directions (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(row, col, grid, visited,each_plant):
      
	# Shorthand for the size of the grid
    num_of_lines = len(grid)
    line_length = len(grid[0])
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
            if 0 <= next_row < num_of_lines and 0 <= next_col < line_length:
				# If the neighbor (next_row, next_col) is part of the same blob
                if grid[next_row][next_col] == each_plant:
					# Add the neighbor (next_row, next_col) to the queue
                    queue.append((next_row, next_col))
                    
                    sides -= 1  # Shared edges reduce the perimeter contribution
                    
        perimeter += sides  # Add remaining sides to the perimeter

    return (area, perimeter)


def main():
    with open("input.txt","r") as f:
        lines = f.readlines()

    line_length = len(lines[0].strip())
    print(line_length)
    visited = []
    all_plants = []
    grid = []
    total = 0

    for line in lines:
        visited.append([False]*(line_length))
        grid.append(list(line.strip()))
        for each_index in line.strip():
              if each_index not in all_plants:
                    all_plants.append(each_index)
        

    print(visited)
    print(grid)
    print(all_plants)

    area = 0
    perimeter = 0

    for each_plant in all_plants:
        for i in range(0,len(lines)):
            for j in range(0,line_length):
                if grid[i][j] != each_plant or visited[i][j]:
                    continue
                area, perimeter = bfs(i, j, grid, visited,each_plant)

                total += area * perimeter
                print(f"Plant: {each_plant}, Area: {area}, Perimeter: {perimeter}")

        
    print(total)


if __name__ == '__main__':
    main()