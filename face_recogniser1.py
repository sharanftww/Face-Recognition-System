import cv2
import pickle

# Camera number: 0 = laptop webcam, 1 = external camera
CAMERA_INDEX = 0

# Serial port of the Arduino. Check Device Manager -> Ports (COM & LPT)
SERIAL_PORT = "COM3"

# Distance limit. LOWER conf = better match (0 = perfect).
# If conf is below THRESHOLD the name is shown, otherwise "unknown".
# Keep this the same as in face_recognise.py
THRESHOLD = 55

# Who is allowed to switch the Arduino ON (folder names in image_data, lowercase).
# Example: ["yourname"] or ["yourname", "brothername"]
# Leave it empty [] to let ANY known person switch it ON.
ALLOWED_NAMES = ["sharan"]

# Every face is resized to this size, same as in face_trainer.py
FACE_SIZE = (200, 200)

# Try to connect to the Arduino. If it is not plugged in, port stays None
# and the program continues with face recognition only (no crash).
port = None
try:
    import serial
    port = serial.Serial(SERIAL_PORT, 9600, timeout=1)
    print(f"Arduino connected on {SERIAL_PORT}")
except Exception as e:
    print(f"Arduino not available ({e}). Running without serial output.")

# Open the camera with the Windows DirectShow backend
video = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
if not video.isOpened():
    print("Error: could not open camera.")
    exit()

# Load the face detector
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load the trained face recogniser model
recognise = cv2.face.LBPHFaceRecognizer_create()
recognise.read("trainner.yml")

# Load the labels and swap them so we can look up a name from an ID
with open("labels.pickle", "rb") as f:
    og_label = pickle.load(f)
labels = {v: k for k, v in og_label.items()}
print("People in the model:", labels)

# Remember the last signal sent, so we write to the Arduino only
# when something changes (not 30 times per second)
last_signal = None

while True:
    check, frame = video.read()
    if not check:
        print("Error: could not read frame.")
        break

    # Convert to gray scale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(80, 80))

    # Assume no allowed person is in front of the camera until we find one
    allowed_person_seen = False

    for x, y, w, h in faces:
        # Cut out the face, resize it and balance the brightness
        # (same preprocessing as in face_trainer.py)
        roi = cv2.resize(gray[y:y+h, x:x+w], FACE_SIZE)
        roi = cv2.equalizeHist(roi)

        # Predict who it is. ID = person number, conf = distance (lower is better)
        ID, conf = recognise.predict(roi)
        name = labels.get(ID, "unknown")
        print(f"closest={name}  conf={conf:.1f}")

        if conf < THRESHOLD:
            text = f"{name} ({conf:.0f})"
            color = (0, 255, 0)      # green = known person

            # Is this person allowed to switch the Arduino ON?
            if len(ALLOWED_NAMES) == 0 or name in ALLOWED_NAMES:
                allowed_person_seen = True
        else:
            text = f"unknown ({conf:.0f})"
            color = (0, 0, 255)      # red = unknown

        # Draw the box and the name on the video
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, color, 2, cv2.LINE_AA)

    # '1' = allowed person visible, '0' = unknown person or nobody visible
    signal = b'1' if allowed_person_seen else b'0'

    # Send only when the signal changes
    if signal != last_signal:
        print(f"Signal: {signal.decode()}")
        if port:
            port.write(signal)
        last_signal = signal

    cv2.imshow("Video", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Turn the Arduino output OFF before quitting
if port:
    port.write(b'0')
    port.close()

# Release the camera and close the windows
video.release()
cv2.destroyAllWindows()