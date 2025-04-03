import raylib as rl
import numpy as np
import random

def main():
    rl.InitWindow(1280, 720, bytes("Raylib Window", "utf-8"))
    rl.SetTargetFPS(60)

    x: int = 1280//2
    y: int = 720//2

    maze, mx, my = genMaze(1280//10, 720//10)

    while not rl.WindowShouldClose():
        rl.PollInputEvents()

        if (rl.IsKeyDown(rl.KEY_W) or rl.IsKeyDown(rl.KEY_UP)) and maze[my-1][mx] != 1:
            my-=1
        if (rl.IsKeyDown(rl.KEY_S) or rl.IsKeyDown(rl.KEY_DOWN)) and maze[my+1][mx] != 1:
            my+=1
        if (rl.IsKeyDown(rl.KEY_A) or rl.IsKeyDown(rl.KEY_LEFT)) and maze[my][mx-1] != 1:
            mx-=1
        if (rl.IsKeyDown(rl.KEY_D) or rl.IsKeyDown(rl.KEY_RIGHT)) and maze[my][mx+1] != 1:
            mx+=1
        print(maze[my][mx])

        rl.BeginDrawing()

        rl.ClearBackground(rl.WHITE)

        for y in range(len(maze)):
                for x in range(len(maze[y])):
                    if maze[y][x] == 1:
                        rl.DrawRectangle(x*10, y*10, 10, 10, rl.BLACK)

        rl.DrawRectangle(mx*10, my*10, 10, 10, rl.RED)

        rl.EndDrawing()

    rl.CloseWindow()


def genMaze(width, height):
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

    return maze.tolist(), entrance_x, entrance_y



if __name__ == "__main__":
    # gen_maze()
    main()