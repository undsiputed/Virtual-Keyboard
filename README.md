# ✨ Gesture-Controlled Virtual Keyboard (Hover Version)

A real-time virtual keyboard you can type on using **just your fingers** — no physical contact required.  
This version uses **hover detection** to type letters, emojis, open apps, and even solve math problems!

---

---

## 🚀 Features
- 🖐️ Hover your index finger over a key for 2.5 seconds to type it
- 🟩 Colorful keyboard rendered with OpenCV
- 😀 Type emojis: 😂 ❤️ 🎉 👍
- ❗ Punctuation: `?` `.` `,` `!`
- 🧮 Calculator mode: toggle with `Calc`, type `2+2=` to get `4`
- 🌐 Open Google, YouTube, and GitHub by hovering over dedicated buttons
- 🔄 `Clear`, `Backspace`, `Space`, and `Enter` all supported
- 💡 No pinch gesture needed — fully hover-controlled

---

## 🧠 Tech Stack
- Python 3.10
- [MediaPipe](https://google.github.io/mediapipe/solutions/hands) for hand tracking
- [OpenCV](https://opencv.org/) for webcam and drawing
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for simulating keypresses
- `webbrowser` module for launching websites

---

## 📁 Project Structure

```
gesture_keyboard/
├── main.py
├── hand_tracking.py
├── virtual_keyboard.py
├── key_press.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/your-username/gesture-keyboard.git
cd gesture-keyboard
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the project
```bash
python main.py
```

---

## 🛑 How to Exit
- Press `Esc` on your keyboard  
- Or close the OpenCV window

---

## 📄 License
This project is open-source under the MIT License.
