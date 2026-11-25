import cv2

# Camera number: 0 = laptop webcam, 1 = external camera.
# Use the index that worked in AccessTo_Webcam.py
CAMERA_INDEX = 0

# Open the camera. CAP_DSHOW is the Windows backend,
# which is usually more reliable for webcams.
video = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

# If the camera could not be opened, print a message and stop the program
# instead of crashing later with a cvtColor error.
if not video.isOpened():
    print(f"Error: could not open camera at index {CAMERA_INDEX}.")
    exit()

# load "haarcascade_frontalface_default.xml" by creating a CascadeClassifier
# object as cascade. This file contains the pre-trained face detector.
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# If the xml file was not found in the folder, the classifier will be empty.
# Stop here and tell the user what is wrong.
if cascade.empty():
    print("Error: could not load haarcascade_frontalface_default.xml. Is it in the same folder?")
    exit()

# This loop runs again and again, once for every frame of the video.
while True:
    # check is True if the frame was read successfully,
    # frame is the actual image from the camera.
    check, frame = video.read()

    # If no frame came from the camera, stop the loop.
    # Without this, the next line would crash on an empty image.
    if not check:
        print("Error: could not read frame.")
        break

    # Image from webcam is in BGR format, i.e. a combination of 3 colours,
    # which requires more computation.
    # So we convert it into a gray scale image, which has only one channel
    # and is faster to process.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detectMultiScale looks for faces in the gray image and returns
    # x, y, w, h for each face: the top-left corner, width and height.
    # scaleFactor = how much the image is shrunk at each search step
    # (smaller = more accurate but slower).
    # minNeighbors = how many overlapping detections are needed to accept a
    # face (higher = fewer false detections).
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    # Go through every detected face and draw a yellow rectangle around it.
    # (0, 255, 255) is the colour in BGR and 3 is the line thickness.
    for x, y, w, h in face:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)

    # Show the frame, with the rectangles drawn on it, in a window called "Video"
    cv2.imshow("Video", frame)

    # Wait 1 millisecond for a key press.
    # If the key is 'q', leave the loop and close the program.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera so other programs can use it
video.release()

# Close all the OpenCV windows
cv2.destroyAllWindows()