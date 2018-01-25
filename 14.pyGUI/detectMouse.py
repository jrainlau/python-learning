import time
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller as keyboard_controller, Listener as keyboard_listener
from pynput.mouse import Button, Controller as mouse_controller, Listener as mouse_listener

event_arr = []
is_auto = [False]

def on_press(key):
    print(key)
    # print(key)
    # if key == Key.cmd:
    #     is_auto[0] = True
    #     for event in event_arr:
    #         mouse_controller().position = event['position']
    #         time.sleep(0.5)
    #         mouse_controller().click(Button.left, 1)
    #         time.sleep(1)

key_listener = keyboard_listener(on_release = on_press)
key_listener.start()

def on_click(x, y, button, pressed):
    # if button == Button.left and not is_auto[0] and not pressed:
    #     event_arr.append({
    #         'event_type': 'click',
    #         'position': (x, y)
    #     })
    pass

with mouse_listener(on_click = on_click) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print('Quite...')