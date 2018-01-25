import os,time
import pyautogui as pag

pag.PAUSE = 1.5

width, height = pag.size()

try:
    while True:
        x, y = pag.position()
        posStr = 'Position: ' + str(x).rjust(4) + ', ' + str(y)
        print(posStr)
        time.sleep(0.2)
        os.system('clear')
except KeyboardInterrupt:
    print('end...')

# for i in range(10):
#       pag.moveTo(300, 300, duration=0.25)
#       pag.moveTo(400, 300, duration=0.25)
#       pag.moveTo(400, 400, duration=0.25)
#       pag.moveTo(300, 400, duration=0.25)