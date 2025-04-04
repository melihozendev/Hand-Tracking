# 🤖 Hand Tracking Project

This project uses hand movement and gesture recognition via webcam to interact with a simple menu interface. It tracks the hand's position and interprets motions (up/down) to navigate through options, and uses open/closed hand states to select them.

---

## 🧠 Description

- Real-time hand tracking using color-based segmentation (black object or glove).
- Gesture-based control: 
  - Move hand **up/down** to navigate.
  - **Close** hand to confirm selection.
- Useful for touchless UI concepts, accessibility, and prototype interaction systems.

---

## 🛠️ Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy

---

## 🖥️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/melihozendev/Hand-Tracking.git
```

2. Navigate to the project folder:

```bash
cd Hand-Tracking
```

3. Install the dependencies (if not already installed):

```bash
pip install opencv-python numpy
```

4. Run the script:

```bash
python Hand_Tracking.py
```

---

## 📹 Demo

[🎥 See It in Action](https://github.com/user-attachments/assets/fca44335-71dc-44d0-b2b8-ca925decf7e0)

---

## ✋ Gesture Controls

- 🖐️ Open Hand + Move Up/Down → Navigate menu options

- ✊ Closed Hand + Not Moving → Lock in and select current option

---

## 🎯 Features
- Real-time webcam-based motion detection

- Direction and hand state feedback overlay

- Simple and intuitive control with only hand gestures
