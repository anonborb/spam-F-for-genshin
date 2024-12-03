import pyautogui, time
from pynput import keyboard

looping = False

def on_press(key):
    global looping
    if key == keyboard.Key.left:
        print("Pausing...")
        looping = False
        # return False
    elif key == keyboard.Key.right:
        print("Starting...")
        looping = True
    elif key == keyboard.Key.backspace:
        print("Exiting...")
        return False


def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        if looping:
            pyautogui.press("f")
            time.sleep(0.1)
        if not listener.running: 
            break

    listener.join()





##### Keyboard Module doesn't work on MACOS #####
# import keyboard
# 
# def loop_f():
#     while True:
#         pyautogui.press("f")
#         time.sleep(0.5)
#         if keyboard.is_pressed('0'):
#             break

# keyboard.add_hotkey('0', loop_f)
# keyboard.wait()


