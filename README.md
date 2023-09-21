# media_control
Purpose: This code uses your computer's webcam to recognize hand gestures and perform specific actions on your computer based on those gestures.

Libraries Used:

cv2 (OpenCV): For handling webcam input and image processing.
mediapipe: For detecting and tracking hand landmarks (finger positions).
keyboard: For simulating keyboard inputs.
time: For introducing delays.
Main Workflow:

Initialize the hand detection model.
Start capturing video from your webcam.
Continuously process each frame of the video:
Detect and track hand landmarks (finger positions).
Based on the detected landmarks, trigger keyboard inputs (e.g., arrow keys, spacebar) to perform actions.
Display the webcam feed with hand landmarks drawn on it.
Continue until you press the 'Esc' key.
When you exit the script, release the webcam resources and close the display window.
Gestures and Actions:

Moving your hand to the left or right triggers corresponding keyboard inputs for left and right.
Moving your hand up or down triggers keyboard inputs for up and down.
Placing your hand at a certain height (between 0.5 and 0.7) triggers a keyboard input for the spacebar.
