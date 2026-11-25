import cv2
import os
import numpy as np
from PIL import Image
import pickle

# Load the face detector
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Create the LBPH face recogniser
recognise = cv2.face.LBPHFaceRecognizer_create()

# Every face is resized to this size so training and recognition match
FACE_SIZE = (200, 200)

def getdata():
    current_id = 0
    label_id = {}     # folder name -> ID number
    face_train = []   # list of face images
    face_label = []   # list of ID numbers

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    my_face_dir = os.path.join(BASE_DIR, "image_data")

    for root, dirs, files in os.walk(my_face_dir):
        for file in files:
            if file.lower().endswith(("png", "jpg", "jpeg")):
                path = os.path.join(root, file)

                # The folder name is the person's name
                label = os.path.basename(root).lower()
                if label not in label_id:
                    label_id[label] = current_id
                    current_id += 1
                ID = label_id[label]

                # Load the image as gray scale
                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, "uint8")

                faces = cascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=5)
                if len(faces) == 0:
                    print(f"Skipped {label}/{file}: no face found")
                    continue

                # Use only the largest face in the photo
                x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

                # Cut out the face, resize it and balance the brightness
                roi = image_array[y:y+h, x:x+w]
                roi = cv2.resize(roi, FACE_SIZE)
                roi = cv2.equalizeHist(roi)

                face_train.append(roi)
                face_label.append(ID)

    # Save the name <-> ID table
    with open("labels.pickle", "wb") as f:
        pickle.dump(label_id, f)

    return face_train, face_label, label_id

faces, ids, label_id = getdata()

if len(faces) == 0:
    print("Error: No faces detected in the training images.")
    exit()

# Show how many usable photos each person has
for name, i in label_id.items():
    print(f"{name}: {ids.count(i)} usable photos")

recognise.train(faces, np.array(ids))
recognise.save("trainner.yml")
print("Training complete. Model saved to 'trainner.yml'.")