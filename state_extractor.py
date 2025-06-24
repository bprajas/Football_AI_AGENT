import cv2
import numpy as np

def extract_local_state(frame):
    """
    Extract normalized coordinates of the ball and closest visible player.
    """
    ball_mask = cv2.inRange(frame, (200, 200, 200), (255, 255, 255))
    ball_coords = cv2.findNonZero(ball_mask)
    if ball_coords is not None:
        ball_avg = np.mean(ball_coords, axis=0)[0]
    else:
        ball_avg = (frame.shape[1] / 2, frame.shape[0] / 2)

    # Placeholder for player detection (you can expand this)
    player_coords = (frame.shape[1] / 3, frame.shape[0] / 2)

    norm = lambda x, d: x / d
    w, h = frame.shape[1], frame.shape[0]
    return [
        norm(ball_avg[0], w), norm(ball_avg[1], h),
        norm(player_coords[0], w), norm(player_coords[1], h),
    ]
