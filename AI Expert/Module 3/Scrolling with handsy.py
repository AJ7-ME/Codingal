import mediapipe as mp
import cv2, time, pyautogui
mp_hands = mp.solutions.hands

#Creates the hand detector max_num_hands=1 means it will only detect one hand at a time
# min_detection_confidence=0.7 means it will only detect hands with a confidence of 70% or higher
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawings = mp.solutions.drawing_utils

#Configurations / Settings
SCROLL_SPEED = 40
SCROLL_DELAY = 0.1
CAM_WIDTH = 640
CAM_HEIGHT = 480
#Configurations / Settings

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    for tips in tips:
        # This checksis the fingertip is above the fingerjoint, Therefore the finger is considered open
        if landmarks[tips].y < landmarks[tips - 2].y:
            fingers.append(1)

    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    
    if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or (handedness == "Left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1)
    return "scroll up" if sum(fingers) == 5 else "scroll down" if sum(fingers) == 0 else "no scroll"
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

#Last scroll : Stores the time when previous scroll was made, to prevent too many scrolls in a short time
last_scroll = p_time = 0
print("Press 'q' to exit")
while cap.isopened():
    success, img = cap.read()
    if not success: break

    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
    results = hands.process(img)
    gesture, handedness = "none", "Unknown"
    if results.multi_hand_landmarks:
        for hand, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):

            handedness = handedness_info.classification[0].label
            gesture = detect_gesture(hand, handedness)
            mp_drawings.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            #this prevents continous scrolling every frame.
            if time.time() - last_scroll > SCROLL_DELAY:
                if gesture == "scroll up":
                    pyautogui.scroll(SCROLL_SPEED)
                    last_scroll = time.time()
                elif gesture == "scroll down":
                    pyautogui.scroll(-SCROLL_SPEED)
                    last_scroll = time.time()

    fps = 1/(time.time()-p_time) if (time.time()-p_time) > 0 else 0
    p_time = time.time()
    cv2.putText(img, f"FPS: {int(fps)} | Hand: {handedness} | Gesture: {gesture}", (10, 30), cv2.        FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.imshow("Gesture Control", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()