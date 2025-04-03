import raylib as rl
import random
from copy import deepcopy
import numpy as np


WIDTH = int(1280)
HEIGHT = int(720)

CELL_SIZE = int(10)

def main():
    rl.InitWindow(1280, 720, bytes("Maze", "utf-8"))

    rl.SetTargetFPS(10)

    mz = generate_maze(WIDTH//CELL_SIZE, HEIGHT//CELL_SIZE)
    solve_maze(mz)
    
    solve = True

    while not rl.WindowShouldClose():
        rl.PollInputEvents()

        if rl.IsKeyDown(rl.KEY_R):
            mz = generate_maze(WIDTH//CELL_SIZE, HEIGHT//CELL_SIZE)
            solve_maze(mz)
        if rl.IsKeyDown(rl.KEY_SPACE):
            solve = not solve

        rl.BeginDrawing()

        rl.ClearBackground(rl.BLACK)

        for y in range(len(mz)):
            for x in range(len(mz[y])):
                if mz[y][x] == 1:
                    rl.DrawRectangle(x*10, y*10, 10, 10, rl.WHITE)
                if mz[y][x] == 2 and solve:
                    rl.DrawRectangle(x*10, y*10, 10, 10, rl.GREEN)
                if mz[y][x] == 3:
                    rl.DrawRectangle(x*10, y*10, 10, 10, rl.PURPLE)
                if mz[y][x] == 4:
                    rl.DrawRectangle(x*10, y*10, 10, 10, rl.ORANGE)

        rl.EndDrawing()

    rl.CloseWindow()


def generate_maze(width, height):
    # Ensure odd dimensions for proper path carving
    width = width if width % 2 == 1 else width - 1
    height = height if height % 2 == 1 else height - 1
    
    # Initialize grid with walls
    maze = np.ones((height, width), dtype=int)

    # Pick random entrance and exit locations on the edges
    def random_edge_position(exclude_wall=None):
        edges = ['top', 'bottom', 'left', 'right']
        if exclude_wall:
            edges.remove(exclude_wall)
        wall = random.choice(edges)

        if wall == 'top':
            return (0, random.randrange(1, width - 1, 2))
        elif wall == 'bottom':
            return (height - 1, random.randrange(1, width - 1, 2))
        elif wall == 'left':
            return (random.randrange(1, height - 1, 2), 0)
        else:  # 'right'
            return (random.randrange(1, height - 1, 2), width - 1)

    entrance_y, entrance_x = random_edge_position()
    exit_y, exit_x = random_edge_position(exclude_wall='top' if entrance_y == 0 else 'bottom' if entrance_y == height - 1 else 'left' if entrance_x == 0 else 'right')

    # Ensure the entrance and exit are open
    maze[entrance_y, entrance_x] = 0
    maze[exit_y, exit_x] = 0

    # Start position for maze generation
    start_x, start_y = entrance_x if entrance_y in [0, height - 1] else entrance_x + 1, entrance_y if entrance_x in [0, width - 1] else entrance_y + 1
    # maze[start_y-1, start_x-1] = 0

    # Stack-based DFS for maze generation
    stack = [(start_x, start_y)]
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # Right, Left, Down, Up

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)  # Randomize directions
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny, nx] == 1:
                # Remove wall between cells
                maze[y + dy // 2, x + dx // 2] = 0
                maze[ny, nx] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()  # Backtrack if no moves are available

    return maze.tolist()

def solve_maze(maze):
    """Solve the maze by finding a path from entrance to exit."""
    
    # Find the entrance and exit coordinates
    entrance = None
    exit = None
    height, width = len(maze), len(maze[0])
    
    # Locate entrance (marked by 0 on the edges) and exit (also marked by 0 on the edges)
    for y in range(height):
        for x in range(width):
            if maze[y][x] != 1:
                if y == 0 or y == height - 1 or x == 0 or x == width - 1:  # Edge positions
                    if entrance is None:
                        entrance = (y, x)
                    elif exit is None and (y != entrance[0] or x != entrance[1]):
                        exit = (y, x)
    
    if not entrance or not exit:
        print("Error: No valid entrance or exit found.")
        return maze

    # Directions for solving the maze: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Function to check if a move is valid
    def valid_move(y, x):
        return 0 <= y < height and 0 <= x < width and maze[y][x] != 1

    # Use DFS to solve the maze
    stack = [entrance]
    visited = set()
    visited.add(entrance)

    while stack:
        y, x = stack[-1]
        
        # Check if we've reached the exit
        if (y, x) == exit:
            break
        
        # Try moving in all four directions
        moved = False
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if valid_move(ny, nx) and (ny, nx) not in visited:
                stack.append((ny, nx))
                visited.add((ny, nx))
                moved = True
                break
        
        # If we can't move in any direction, backtrack
        if not moved:
            stack.pop()
    
    # Mark the solved path with 2s
    for y, x in stack:
        maze[y][x] = 2
    
    maze[int(entrance[0])][int(entrance[1])] = 3
    maze[int(exit[0])][int(exit[1])] = 4

    return maze

if __name__ == "__main__":
    # gen_maze()
    main()