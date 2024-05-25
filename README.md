Project Description:

This project utilizes the MediaPipe library and OpenCV to perform real-time hand gesture recognition for controlling keyboard inputs. The program captures video from the webcam, detects hand landmarks using the MediaPipe Hands model, and interprets specific gestures to trigger keyboard commands.

Features:

Hand Detection: Utilizes the MediaPipe Hands model to detect and track hand landmarks in the webcam feed.

Gesture Recognition: Interprets hand gestures, such as moving left, right, up, down, and performing a hand gesture to trigger keyboard commands.

Dynamic Keyboard Control: Translates detected hand gestures into corresponding keyboard commands for left, right, up, down movements, and space bar press.

Implementation Details:

MediaPipe Integration: Utilizes the MediaPipe library to access the pre-trained hand detection model for real-time hand landmark tracking.

OpenCV Usage: Captures video frames from the webcam and processes them using OpenCV for display and image manipulation.

Keyboard Control: Utilizes the keyboard module to trigger keyboard events based on detected hand gestures.

Continuous Execution: Runs in a loop to continuously capture and process video frames until the user exits the program.

Usage:

Execution: Run the script to start real-time hand gesture recognition and keyboard control.

Hand Gestures: Perform hand gestures within the webcam frame to trigger keyboard commands.

Keyboard Interaction: Observe the keyboard responses corresponding to the detected hand gestures.

Dependencies:

OpenCV (cv2)

MediaPipe (mediapipe)

keyboard module

time module
