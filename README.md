# Football_AI_AGENT

###  Purpose
Build a football-playing neural agent that watches a match through a camera, understands the game, and controls EA FC 24 using a game controller.

---

##  Components
- `brain.py`: Neural Network (PyTorch)
- `screen_tracker.py`: Visual input → state vector
- `control_loop.py`: Orchestrator
- `controller_arduino.ino`: Arduino controller interface

---

##  Setup Instructions
1. Flash Arduino with `controller_arduino.ino`
2. Connect webcam focused on your TV screen
3. Run `control_loop.py` — it will start tracking and sending controller inputs
4. Train NN using `train_brain.py` (or use dummy for now)

---

##  Dependencies
- Python 3.9+
- PyTorch
- OpenCV (`pip install opencv-python`)
- Arduino IDE
