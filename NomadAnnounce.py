import pyautogui
from pynput.keyboard import *
from pynput.keyboard import Key, Controller
import time
import json

#  ======== settings ========
delay = 120  # in seconds
message = 'samplemsg'
footer = ''
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

keyboard = Controller()

# keybinds
pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("Started")
    elif key == pause_key:
        pause = True
        print("Stopped")
    elif key == exit_key:
        running = False
        print("Exiting...")

# welcome message
def display_controls():
    print("// Hope Announce")
    print("// - Settings: ")
    print("\t message = " + message)
    print("\t delay = " + str(delay) + " seconds" + '\n')

    print("// - Controls:")
    print("\t F1 = Start")
    print("\t F2 = Pause")
    print("\t ESC = Exit")
    print("-----------------------------")
    print('Press F1 to start ...')

# message typer
def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.typewrite(message)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(delay)

    lis.stop()

# run
if __name__ == "__main__":
    main()