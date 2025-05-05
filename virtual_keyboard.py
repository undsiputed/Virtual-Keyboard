import webbrowser
import cv2


class VirtualKeyboard:
    def __init__(self):
        self.keys = [
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM"),
   ["Space", "Backspace","Google", "YouTube", "GitHub", "Clear", "Calc", "=", "?", ".", ",", "!", 
 "😀", "😂", "❤️", "👍", "🎉"]
        ]

        self.key_coords = []
        self.colors = [
            (255, 105, 180), (135, 206, 250), (144, 238, 144),
            (255, 165, 0), (221, 160, 221), (255, 255, 0),
            (173, 216, 230), (255, 182, 193), (255, 215, 0),
            (152, 251, 152), (240, 128, 128)
        ]

        start_x = 100
        for row_idx, row in enumerate(self.keys):
            y = 100 + row_idx * 80
            row_coords = []
            for col_idx, key in enumerate(row):
                x = 100 + col_idx * 120 if row_idx == 3 else 100 + col_idx * 70
                self.key_coords.append((key, x, y))

    def draw_keys(self, frame):
        for i, (key, x, y) in enumerate(self.key_coords):
            color = self.colors[i % len(self.colors)]
            cv2.rectangle(frame, (x, y), (x+100, y+60), color, -1)
            cv2.putText(frame, key, (x+10, y+40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        return frame

    def get_hovered_key(self, finger_pos):
        x_f, y_f = finger_pos
        for key, x, y in self.key_coords:
            if x < x_f < x + 100 and y < y_f < y + 60:
                return key
        return None

    def highlight_key(self, frame, key):
        for k, x, y in self.key_coords:
            if k == key:
                cv2.rectangle(frame, (x, y), (x+100, y+60), (0, 255, 0), -1)
                cv2.putText(frame, key, (x+10, y+40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        return frame
