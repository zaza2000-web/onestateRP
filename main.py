import pyautogui
import time
import keyboard
import sys
import pygetwindow as gw

print("Запуск начнется через 5 секунд")
time.sleep(5)

paused = False
max_reports = 3

def go_to_fraction():
    time.sleep(0.5)
    pyautogui.click(1844, 56)
    time.sleep(0.5)
    pyautogui.click(1760, 201)
    time.sleep(0.5)
    pyautogui.click(151, 582)

def take_position():
    time.sleep(1)
    print(pyautogui.position())

def is_ldplayer_active():
    active_window = gw.getActiveWindow()
    return active_window is not None and "LDPlayer" in active_window.title

def get_report():
    time.sleep(0.1)
    pyautogui.click(1234, 20)
    time.sleep(0.3)
    pyautogui.click(423, 289)
    time.sleep(0.1)
    pyautogui.click(1289, 289)



if is_ldplayer_active():
    while True:
        if keyboard.is_pressed("F4"):
            paused = True
            print("Скрипт приостановлен. Нажмите F5 для возобновления.")
            time.sleep(0.5)

        elif keyboard.is_pressed("F5"):
            paused = False
            print("Скрипт возобновлен.")
            time.sleep(0.5)

        if paused:
            continue

        elif keyboard.is_pressed("f"):
            while keyboard.is_pressed("f"):
                go_to_fraction()

        elif keyboard.is_pressed("o"):
            while keyboard.is_pressed("o"):
                take_position()

        elif keyboard.is_pressed("c"):

            while keyboard.is_pressed("c"):
                get_report()
           
        
