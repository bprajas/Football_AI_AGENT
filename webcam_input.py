import cv2

def get_frame():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Webcam not found.")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise Exception("Failed to grab frame")
    return frame

def crop_visible_pitch(frame):
    h, w, _ = frame.shape
    # You may need to calibrate this box
    return frame[int(h*0.3):int(h*0.9), int(w*0.1):int(w*0.9)]
