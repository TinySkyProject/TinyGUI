import time
import keyboard
from colorama import Fore, Style, init
import pygame
import string

init()
pygame.mixer.init()

GUIS = []

EXIT = "EXIT"

class Label:
    def __init__(self, GUI, text: str, x: int, y: int, color = Fore.WHITE):
        if GUI.deleted:
            return
        index = [text, round(x), round(y), color, "text"]
        GUI.UIS.append(index)
        self.index = GUI.UIS.index(index)
        
    def Edit(self, GUI, text: str, x: int, y: int, color = Fore.WHITE):
        if GUI.deleted:
            return
        if text == None:    text = GUI.UIS[self.index][0]
        if x == None:   x = GUI.UIS[self.index][1]
        if y == None:    y = GUI.UIS[self.index][2]
        if color == None:   color = GUI.UIS[self.index][3]
        GUI.UIS[self.index][0] = text
        GUI.UIS[self.index][1] = x
        GUI.UIS[self.index][2] = y
        GUI.UIS[self.index][3] = color

class Main:
    def __init__(self, GUI_NAME: str = "GUI__G", GUI_WIDTH: int = 168, GUI_HEIGHT: int = 35, fps_limit: float = 60):
        if GUI_NAME in GUIS:
            return
        self.deleted = False
        self.GUI_NAME = GUI_NAME
        self.GUI_WIDTH = GUI_WIDTH
        self.GUI_HEIGHT = GUI_HEIGHT
        self.UIS = []
        self.last_update_time = time.time()
        self.fps_limit = fps_limit
        self.time_per_update = 1.0 / self.fps_limit

        for _ in range(188):
            print("\n" * 40 + "Loading..." + "\n" * 40)
            time.sleep(0)
            print("\n" * 40 + "Loading.." + "\n" * 40)
            time.sleep(0)
            print("\n" * 40 + "Loading." + "\n" * 40)
            time.sleep(0)
            print("\n" * 40 + "Loading.." + "\n" * 40)
            time.sleep(0)

        GUIS.append(GUI_NAME)
        
    def delete(self):
        if self.deleted:
            return
        GUIS.remove(self.GUI_NAME)
        self.deleted = True

    def collidedwith(self, index1: int, index2: int):
        if self.deleted:
            return False

        if index1 < 0 or index1 >= len(self.UIS) or index2 < 0 or index2 >= len(self.UIS):
            return False
        
        ui1 = self.UIS[index1]
        ui2 = self.UIS[index2]

        text1, x1, y1 = ui1[0], ui1[1], ui1[2]
        width1 = len(text1)

        text2, x2, y2 = ui2[0], ui2[1], ui2[2]
        width2 = len(text2)

        if y1 == y2 and (x1 < x2 + width2 and x1 + width1 > x2):
            return True

        return False

    def update(self):
        if self.deleted:
            return

        time.sleep(self.time_per_update)

        current_time = time.time()

        frame_time = current_time - self.last_update_time

        if current_time - self.last_update_time < self.time_per_update:
            return

        self.last_update_time = current_time

        if frame_time > 0:
            fps = round(1 / frame_time)
            fpsshowtxt = f"FPS: {fps}"
        else:
            fpsshowtxt = "FPS: 0"

        num = self.GUI_WIDTH - len(self.GUI_NAME) - 11 - len(fpsshowtxt)
        left_spacing = num // 2
        right_spacing = num // 2

        if num % 2 != 0:
            left_spacing += 1
        
        if left_spacing + len(fpsshowtxt) + right_spacing > self.GUI_WIDTH:
            excess = (left_spacing + len(fpsshowtxt) + right_spacing) - self.GUI_WIDTH
            if left_spacing > excess:
                left_spacing -= excess
            else:
                left_spacing = 0
                right_spacing = self.GUI_WIDTH - len(fpsshowtxt) - left_spacing

        print("")
        print(f"{self.GUI_NAME}{' ' * left_spacing}{fpsshowtxt}{' ' * right_spacing}ESC TO EXIT")
        print(f"{'-' * self.GUI_WIDTH}")

        for i in range(self.GUI_HEIGHT + 1):  
            added = False
            finaltext = [" "] * (self.GUI_WIDTH + 1) 

            for ui in self.UIS:  
                if round(ui[2]) == i:
                    added = True
                    if round(ui[1]) < self.GUI_WIDTH:
                        for index, char in enumerate(ui[0]):
                            if round(ui[1]) + index <= self.GUI_WIDTH:  
                                finaltext[round(ui[1]) + index] = ui[3] + char

            if added:
                textToPrint = "".join(finaltext)
                if len(textToPrint) > self.GUI_WIDTH:
                    finaltext = finaltext[:self.GUI_WIDTH]
                print("".join(finaltext))
            else:
                print("")
        print(Style.RESET_ALL)
        print(f"{'-' * self.GUI_WIDTH}")

def Is_Pressed(Key: str):
    return keyboard.is_pressed(Key)

def Sound(location: str):
    return pygame.mixer.Sound(location)

def PlaySound(sound):
    sound.play()

def GetPressedKeys():
    pressed = [key for key in string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' \t\n\r' if Is_Pressed(key)]
    if Is_Pressed("Escape"):
        pressed.append("EXIT")
    elif Is_Pressed("Ctrl"):
        pressed.append("ctrl")
    elif Is_Pressed("Shift"):
        pressed.append("shift")
    elif Is_Pressed("Space"):
        pressed.append("space")
    return pressed
