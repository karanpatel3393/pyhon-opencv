import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('zulin.mp4')

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

# Loop to read frames and display them
while True:
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame. Exiting ...")
        break

    # Display the frame
    cv2.imshow('Video Playback', frame)

    # Press 'q' to exit the video playback
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()
