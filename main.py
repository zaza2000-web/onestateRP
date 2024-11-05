import pyautogui
import time
import keyboard
import sys
import pygetwindow as gw

print("Запуск начнется через 5 секунд")
time.sleep(5)

paused = False

def go_to_fraction():
    time.sleep(0.5)
    menu_x, menu_y = 1844, 56
    pyautogui.click(menu_x, menu_y)
    time.sleep(0.5)
    fraction_x, fraction_y = 1760, 201
    pyautogui.click(fraction_x, fraction_y)
    time.sleep(0.5)
    player_list_x, player_list_y = 151, 582
    pyautogui.click(player_list_x, player_list_y)

def take_position():
    time.sleep(1)
    print(pyautogui.position())

def is_ldplayer_active():
    active_window = gw.getActiveWindow()
    return active_window is not None and "LDPlayer" in active_window.title
def get_report():
    report_position_x,report_position_y = 1234,20
    target_position_x,target_position_y = 423,289
    get_report_position_x,get_report_position_y = 1289,289
    time.sleep(0.1)
    pyautogui.click(report_position_x,report_position_y)
    time.sleep(0.3)
    pyautogui.click(target_position_x,target_position_y)
    time.sleep(0.1)
    pyautogui.click(get_report_position_x,get_report_position_y)




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
