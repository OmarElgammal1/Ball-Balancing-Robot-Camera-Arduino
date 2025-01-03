import cv2
import matplotlib.pyplot as plt
import numpy as np

# Open the default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

print("Press Ctrl+C to exit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert BGR to RGB for Matplotlib display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect white color (dummy example for ping pong ball detection)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 200])
        upper_white = np.array([180, 55, 255])
        mask = cv2.inRange(hsv, lower_white, upper_white)

        # Display using Matplotlib
        plt.subplot(1, 2, 1)
        plt.title("Camera Feed")
        plt.imshow(frame_rgb)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title("Mask")
        plt.imshow(mask, cmap="gray")
        plt.axis('off')

        plt.pause(0.001)
        plt.clf()

except KeyboardInterrupt:
    print("Exiting...")

finally:
    cap.release()
    plt.close()
