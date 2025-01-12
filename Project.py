import tinygui

GUI_WIDTH = 237
GUI_HEIGHT = 60
fps_limit = 60

gui = tinygui.Main("GUI", GUI_WIDTH, GUI_HEIGHT, fps_limit)

coinX = 0
coinY = GUI_HEIGHT
coinText = "©"
coinColor = tinygui.Fore.YELLOW
coin = tinygui.Label(gui, coinText, coinX, coinY, coinColor)

playerX = 0
playerY = 0
playerText = "|"
playerColor = tinygui.Fore.RED
player = tinygui.Label(gui, playerText, playerX, playerY, playerColor)

coins = 0

coinShower = tinygui.Label(gui, "Coins: 0", 0, 0, clicker.Fore.YELLOW)

is_shifting = False
is_jumping = False
is_falling = False
is_sliding = False
was_sliding = False

wait_frame = 0
wanted_frame = 0
jump_frame = 20

frame_set = None

running = True
while running:
    for key in tinygui.GetPressedKeys():
        if key == tinygui.EXIT:
            running = False
        if key == "a":
            if not is_shifting:
                playerText = "\\"
                if was_sliding:
                    is_sliding = False
                    was_sliding = False
            else:
                playerText = "_"
                if not is_sliding:
                    is_sliding = True
                    was_sliding = True
            if is_sliding:
                playerX -= 1.5
            else:
                playerX -= 1
            if playerX < 0:
                playerX = 0
        elif key == "d":
            if not is_shifting:
                playerText = "/"
                if was_sliding:
                    is_sliding = False
                    was_sliding = False
            else:
                playerText = "_"
                if not is_sliding:
                    is_sliding = True
                    was_sliding = True
            if is_sliding:
                playerX += 1.5
            else:
                playerX += 1
            if playerX > GUI_WIDTH - 1:
                playerX = GUI_WIDTH - 1

    if tinygui.Is_Pressed("Space"):
        if not is_falling:
            jump_frame += 1
            if 20 > jump_frame:
                currectY = playerY
                if jump_frame > 10:
                    playerY -= 0.5
                else:
                    playerY -= 1
                if playerY < 0:
                    playerY = 0
                else:
                    is_jumping = True
            else:
                is_jumping = False
    else:
        is_jumping = False
    
    if tinygui.Is_Pressed("Shift"):
        is_shifting = True
    else:
        is_shifting = False
    
    if not is_jumping:
        if is_shifting:
            playerY += 2
        else:
            if jump_frame > 15:
                playerY += 0.8
            elif jump_frame > 10:
                playerY += 0.75
            elif jump_frame > 5:
                playerY += 0.5
            else:
                playerY += 0.25
        if playerY > GUI_HEIGHT:
            playerY = GUI_HEIGHT
            is_falling = False
            jump_frame = 0
        else:
            is_falling = True

    if gui.collidedwith(player.index, coin.index):
        coins += 1
        coin.Edit(gui, coinText, -1, -1, coinColor)
        wait_frame = 0
        wanted_frame = 300
        frame_set = "coinrespawn"

    wait_frame += 1
    if wait_frame >= wanted_frame:
        if frame_set == "coinrespawn":
            coin.Edit(gui, coinText, coinX, coinY, coinColor)

    if not clicker.Is_Pressed("d") and not clicker.Is_Pressed("a"):
        if is_shifting:
            playerText = "_"
        else:
            playerText = "|"

    coinShower.Edit(gui, f"Coins: {coins}", 0, 0, clicker.Fore.YELLOW)
    player.Edit(gui, playerText, playerX, playerY, playerColor)
    gui.update()
    
gui.delete()
