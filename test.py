from pynput import keyboard

keyPressed = True

def on_press(key):
    global keyPressed
    if keyPressed == True:
        keyPressed = False
        try:
            print('{0} pressed'.format(key.char))
        except AttributeError:
            print('{0} pressed'.format(key))

def on_release(key):
    global keyPressed
    keyPressed = True
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()
