import cv2
import mediapipe as mp
import keyboard
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize the hand detection model
hands = mp_hands.Hands(static_image_mode=False, max_num_hands =1 , min_detection_confidence=0.9)

# Initialize the video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        
        continue
 
    # Flip the image horizontally for a more intuitive selfie-view
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB and process it with Mediapipe
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the x and y coordinates of the hand landmarks
            x, y, = [], []
            for landmark in hand_landmarks.landmark:
                x.append(landmark.x)
                y.append(landmark.y)
                print(x,y)
            if min(x) < 0.2:
                keyboard.press('left')
                keyboard.release('left')
            elif max(x) > 0.8:
                keyboard.press('right')
                keyboard.release('right')

            #  Determine whether the hand is up or down in the image
            if  min(y) < 0.2:
                keyboard.press('up')
                keyboard.release('up')
            elif max(y) > 0.8:
                keyboard.press('down')
                keyboard.release('down')

            if min(y)>0.5 and min(y)<0.7:
                keyboard.press('space')
                keyboard.release('space')
                time.sleep(2)




    # Display the image
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break


# Release resou rces
cv2.release()
cv2.destfroyAllWindows()