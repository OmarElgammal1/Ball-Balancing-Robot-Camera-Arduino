import cv2
import numpy as np

# Open the default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

print("Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define HSV range for detecting white color
    # Adjust these values based on your lighting conditions
    lower_white = np.array([0, 0, 200])  # Lower bound for white
    upper_white = np.array([180, 55, 255])  # Upper bound for white

    # Create a mask for white color
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Remove noise with morphological operations
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours to find the largest one
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 350:  # Adjust the threshold based on the ball size
            # Get the bounding circle for the largest contour
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Draw the circle and the center point
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            cv2.putText(frame, "Ping Pong Ball", (center[0] - 50, center[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame and the mask
    cv2.imshow("Camera Feed", frame)
    cv2.imshow("Mask", mask)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
