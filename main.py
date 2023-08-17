import cv2

# Load the image
img = cv2.imread('dhoni.jpg')

# Display the image in a window named "My Image"
cv2.imshow('dhoni', img)

# Wait indefinitely for a key event
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

