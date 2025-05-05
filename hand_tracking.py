import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        return self.results.multi_hand_landmarks

    def get_index_finger_pos(self, hand_landmarks):
        if hand_landmarks:
            h, w, _ = 480, 640, 3
            lm = hand_landmarks[0].landmark[8]
            return int(lm.x * w), int(lm.y * h)
        return None