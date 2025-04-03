import raylib as rl

def main():
    rl.InitWindow(1280, 720, bytes("Raylib Window", "utf-8"))
    rl.SetTargetFPS(60)

    x: int = 1280//2
    y: int = 720//2



    while not rl.WindowShouldClose():
        rl.PollInputEvents()

        if rl.IsKeyDown(rl.KEY_W) or rl.IsKeyDown(rl.KEY_UP):
            y-=10
        if rl.IsKeyDown(rl.KEY_S) or rl.IsKeyDown(rl.KEY_DOWN):
            y+=10
        if rl.IsKeyDown(rl.KEY_A) or rl.IsKeyDown(rl.KEY_LEFT):
            x-=10
        if rl.IsKeyDown(rl.KEY_D) or rl.IsKeyDown(rl.KEY_RIGHT):
            x+=10

        rl.BeginDrawing()

        rl.ClearBackground(rl.BLACK)

        rl.DrawRectangle(x, y, 100, 100, rl.ORANGE)

        rl.EndDrawing()

    rl.CloseWindow()


if __name__ == "__main__":
    main()