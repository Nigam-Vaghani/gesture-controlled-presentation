# Gesture-Controlled Presentation System 🎯

A computer vision project using Python, OpenCV, and CVZone that allows users to control PowerPoint-style presentations with hand gestures via webcam.

## 🔥 Features

- 📸 Real-time hand tracking using webcam or mobile camera
- ✋ Swipe left/right with gestures to move slides
- 🟢 Draw annotations using index finger
- ❌ Clear annotations with a specific gesture
- 🎤 Voice command integration (optional extension)
- 📱 Compatible with mobile camera via IP webcam

## 🛠️ Tech Stack

- Python
- OpenCV
- CVZone
- MediaPipe
- Numpy

## 📦 Requirements

Install the required packages using:

```bash
pip install -r requirements.txt

Or manually:
pip install opencv-python cvzone mediapipe numpy

📁 Folder Structure
gesture-controlled-presentation/
├── Presentation/          # Folder with slide images
├── main.py                # Main gesture control script
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
🖥️ How to Run
Place your slides (as .jpg or .png) in the Presentation folder.

Run the project:
python main.py

Use hand gestures to control your presentation:
Right swipe → Next slide
Left swipe → Previous slide
Index finger up → Draw
Index + Middle up → Stop drawing
Open hand → Clear drawings

📱 Use Mobile as Camera (Optional)
Install IP Webcam on Android, and connect with this script by updating:

cap = cv2.VideoCapture("http://<your-phone-ip>:8080/video")


🚀 Future Extensions
Translate sign language gestures into text
Voice commands integration
Slide click + laser pointer gesture
Export drawings as annotation layer

## you can check demo video: sample.mp4


🧑‍💻 Author
Nigam Vaghani

```

