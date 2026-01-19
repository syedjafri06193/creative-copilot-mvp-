import cv2
import numpy as np

def analyze_video(path):
    cap = cv2.VideoCapture(path)
    frames = []
    colors = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame)
        avg_color = frame.mean(axis=(0,1))
        colors.append(avg_color)

    cap.release()

    colors = np.array(colors)
    pacing = len(frames)
    avg_color = colors.mean(axis=0)

    return {
        "frames": pacing,
        "color": avg_color.tolist()
    }
