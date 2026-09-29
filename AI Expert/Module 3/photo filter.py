import cv2, time, numpy as np
import mediapipe as mp
H = mp.solutions.hands
TIP = H.HandLandmark
ids = {
    "thumb": TIP.THUMB_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP
}
hands = H.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6)
draw = mp.solutions.drawing_utils
pairs = {"middle":("SEPIA", "NEGATIVE"), "ring":("BLUR", "GLITCH"), "pinky":("EDGE", "CARTOON")}
st = {k:0 for k in pairs}
cur = "SEPIA"
#SETTINGS
#1 DEB = 0.6 debounce time. A filter