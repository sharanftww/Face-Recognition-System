import cv2
import pickle

CAMERA_INDEX = 0     # use the index that worked for you

# Distance limit. LOWER conf = better match (0 = perfect).
# conf below THRESHOLD -> show the name, otherwise -> "unknown".
THRESHOLD = 50

FACE_SIZE = (200, 200)

video = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
if not video.isOpened():
    print("Error: could not open camera.")
    exit()

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognise = cv2.face.LBPHFaceRecognizer_create()
recognise.read("trainner.yml")

# Load the labels and swap them so we can look up a name from an ID
with open("labels.pickle", "rb") as f:
    og_label = pickle.load(f)
labels = {v: k for k, v in og_label.items()}
print("People in the model:", labels)

while True:
    check, frame = video.read()
    if not check:
        print("Error: could not read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(80, 80))

    for x, y, w, h in faces:
        # Same preprocessing as in the trainer
        roi = cv2.resize(gray[y:y+h, x:x+w], FACE_SIZE)
        roi = cv2.equalizeHist(roi)

        ID, conf = recognise.predict(roi)
        name = labels.get(ID, "unknown")

        # Accept only if the distance is small enough
        if conf < THRESHOLD:
            text = f"{name} ({conf:.0f})"
            color = (0, 255, 0)      # green = known person
        else:
            text = f"unknown ({conf:.0f})"
            color = (0, 0, 255)      # red = unknown

        # Print so you can tune the threshold
        print(f"closest={name}  conf={conf:.1f}")

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, color, 2, cv2.LINE_AA)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()