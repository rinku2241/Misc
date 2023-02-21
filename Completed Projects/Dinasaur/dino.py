from array import array
from ast import main
import pyautogui
from PIL import Image, ImageGrab
import time 
from numpy import asarray

def hit(key):

    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(280,500):
            for j in range(610,680):
                if data[i, j] < 100:
                    return True
    return False
    
if __name__=="__main__":
    print('hey dino game about to start in 3 seconds ')
    time.sleep(3)


    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit('up')

# image = ImageGrab.grab().convert('L')
# data = image.load()
# for i in range(280,500):
#         for j in range(610,680):
#             data[i, j] =0
# image.show()
