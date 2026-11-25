import cv2

# Try changing this index if the external camera is not detected
camera_index =  0 

# Initialize the camera capture with DirectShow backend for better compatibility on Windows
cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

# Check if the camera opened successfully
if not cap.isOpened():
    print(f"Error: Could not open camera at index {camera_index}.")
    exit()

# Set resolution explicitly for the external camera (e.g., Logitech 720p)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the camera feed
    cv2.imshow('Camera Input', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
