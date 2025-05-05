import pyautogui
import time
import webbrowser

class KeyPresser:
    def __init__(self):
        self.last_key = ""
        self.last_time = 0

    def press_key(self, key):
        current_time = time.time()
        if key != self.last_key or current_time - self.last_time > 1:
            self.last_key = key
            self.last_time = current_time

            if key == "Space":
                pyautogui.write(" ")
            elif key == "Backspace":
                pyautogui.press("backspace")
            elif key == "Enter":
                pyautogui.press("enter")
            elif key == "Google":
                webbrowser.open("https://www.google.com")
            elif key == "YouTube":
                webbrowser.open("https://www.youtube.com")
            elif len(key) == 1:
                pyautogui.write(key.lower())
