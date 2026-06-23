import pyautogui
import cv2
import numpy as np
import time
import keyboard  

def draw_gartic_pixel(image_path, scale=0.2):

    img = cv2.imread(image_path, 0)
    if img is None:
        print("Resim bulunamadı!")
        return

    img = cv2.resize(img, (0,0), fx=scale, fy=scale)
    _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    print(">>> Fareyi Gartic BEYAZ ALANIN SOL ÜST köşesine koy ve 3 sn bekle...")
    time.sleep(3)
    start_x, start_y = pyautogui.position()
    print("Başladı! (Çıkmak için Q bas | Ctrl = hızlandır)")

    height, width = thresh.shape

    for y in range(height):
        for x in range(width):

  
            if keyboard.is_pressed("q"):
                print("Q basıldı, çıkılıyor...")
                return

            if keyboard.is_pressed("ctrl"):
                i =0
                pyautogui.PAUSE = i
                i += 1
            else:
                pyautogui.PAUSE = 0.02

            if thresh[y, x] == 0:
                pyautogui.click(start_x + x, start_y + y)
    
    print("Bitti!")
print("Başlatmak için W bas...")

while True:
    if keyboard.is_pressed("w"):
        print("W basıldı, çizim başlıyor...")
        time.sleep(0.5)
        draw_gartic_pixel('m.png', scale=1)
        break