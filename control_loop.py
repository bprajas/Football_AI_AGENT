from webcam_input import get_frame, crop_visible_pitch
from state_extractor import extract_local_state
from brain import load_model
import serial
import time
import torch

model = load_model("weights/brain.pth")
ser = serial.Serial("/dev/ttyUSB0", 9600)

while True:
    frame = get_frame()
    cropped = crop_visible_pitch(frame)
    state = extract_local_state(cropped)
    x = torch.tensor(state, dtype=torch.float32)
    probs = model(x)

    action = torch.argmax(probs).item()
    ser.write((str(action) + "\n").encode())
    time.sleep(0.1)
