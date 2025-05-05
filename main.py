from hand_tracking import HandTracker
from virtual_keyboard import VirtualKeyboard
from key_press import KeyPresser
import cv2
import time
import webbrowser

# Initialize modules
tracker = HandTracker()
keyboard = VirtualKeyboard()
presser = KeyPresser()

# Start webcam
cap = cv2.VideoCapture(0)

typed_text = ""
last_pressed = ""
last_press_time = 0
calc_mode = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 720))

    hands = tracker.find_hands(frame)
    index_finger_pos = tracker.get_index_finger_pos(hands)

    frame = keyboard.draw_keys(frame)

    if index_finger_pos:
        hovered_key = keyboard.get_hovered_key(index_finger_pos)
        if hovered_key:
            frame = keyboard.highlight_key(frame, hovered_key)

            # Add hover delay (2.5 sec)
            current_time = time.time()
            if hovered_key != last_pressed or (current_time - last_press_time) > 2.5:
                presser.press_key(hovered_key)
                last_pressed = hovered_key
                last_press_time = current_time

                # Update text or trigger actions
                if hovered_key == "Space":
                    typed_text += " "
                elif hovered_key == "Backspace":
                    typed_text = typed_text[:-1]
                elif hovered_key == "Enter":
                    typed_text += "\n"
                elif hovered_key == "Clear":
                    typed_text = ""
                elif hovered_key == "Calc":
                    calc_mode = not calc_mode
                    typed_text = "" if calc_mode else typed_text
                elif hovered_key == "=" and calc_mode:
                    try:
                        expression = typed_text.replace("×", "*").replace("÷", "/")
                        typed_text = str(eval(expression))
                    except:
                        typed_text = "Error"
                elif hovered_key == "Google":
                    webbrowser.open("https://www.google.com")
                elif hovered_key == "YouTube":
                    webbrowser.open("https://www.youtube.com")
                elif hovered_key == "GitHub":
                    webbrowser.open("https://github.com")
                else:
                    typed_text += hovered_key

    # Show typed text
    cv2.rectangle(frame, (100, 600), (1150, 680), (0, 0, 0), -1)
    cv2.putText(frame, typed_text[-40:], (110, 660),
                cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 3)

    cv2.imshow("Gesture Keyboard", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
