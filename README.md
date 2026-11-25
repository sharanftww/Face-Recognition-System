# Face Recognition-Based Access Control System

A real-time face recognition system developed using Python and OpenCV that identifies registered individuals through a webcam. The system uses Haar Cascade for face detection and the LBPH (Local Binary Patterns Histograms) algorithm for face recognition.

The project integrates with an Arduino microcontroller through serial communication to control an LED based on face recognition results, providing a visual indication of authorization status.

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Execution](#execution)
- [Expected Output](#expected-output)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Project Overview

This project demonstrates a computer vision-based identity recognition system that uses a webcam to detect and recognize registered individuals.

It combines face detection, face recognition and Arduino hardware integration to provide an LED-based visual indication when an individual is recognized as authorized.

## Problem Statement

Manual identity verification can be time-consuming and requires human involvement. This project explores an automated approach using computer vision to identify registered individuals and provide a corresponding hardware indication.

## Objectives

- Detect human faces through a webcam.
- Train a face recognition model using custom image data.
- Identify registered individuals.
- Distinguish recognized individuals from unknown faces.
- Integrate Arduino for LED-based authorization indication.

## Features

- Real-time face detection.
- Haar Cascade frontal-face detection.
- LBPH-based face recognition.
- Custom face dataset training.
- Recognition of registered and unknown individuals.
- Arduino serial communication.
- LED-based visual indication.

## How It Works

1. The webcam captures live video.
2. Haar Cascade detects faces in the video frames.
3. Detected faces are preprocessed for recognition.
4. The trained LBPH model compares the detected face with stored training data.
5. The system identifies the person or marks the face as unknown.
6. The Arduino receives a serial signal based on the authorization result.
7. The LED indicates the authorization status.

## Technologies Used

- Python
- OpenCV
- Haar Cascade
- LBPH Face Recognizer
- Arduino
- Serial Communication

## Project Structure

```text
Face-Recognition-System/
│
├── AccessTo_Webcam.py
├── Face_identification.py
├── face_trainer.py
├── face_recognise.py
├── face_recogniser1.py
│
├── haarcascade_frontalface_default.xml
├── labels.pickle
├── trainner.yml
│
├── image_data/
├── ard_chaser/
│
└── README.md
```

## Installation

### Prerequisites

- Windows 10/11
- Python 3
- Visual Studio Code
- Webcam
- Arduino board (for hardware integration)
- Arduino IDE

### 1. Clone the Repository

Open the VS Code terminal and execute:

```bash
git clone https://github.com/sharanftww/Face-Recognition-System.git
```

Navigate to the project directory:

```bash
cd Face-Recognition-System
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

### 3. Install Required Libraries

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the required Python libraries:

```bash
pip install opencv-contrib-python numpy Pillow pyserial
```

**Note:** OpenCV Contrib is required for the LBPH face recognizer. Avoid installing `opencv-python` alongside `opencv-contrib-python` in the same environment.

## Execution

Run the following Python scripts from the main project directory in the specified order.

### Step 1: Test Webcam Access

```bash
python AccessTo_Webcam.py
```

This script opens the webcam and displays the live video feed.

Press `q` to close the camera window.

### Step 2: Test Face Detection

```bash
python Face_identification.py
```

This script uses Haar Cascade to detect faces and display bounding boxes around them.

Press `q` to exit.

### Step 3: Train the Face Recognition Model

```bash
python face_trainer.py
```

This script:

- Loads training images from the `image_data/` directory.
- Detects and preprocesses faces.
- Trains the LBPH face recognition model.
- Generates the following files:

  - `trainner.yml`
  - `labels.pickle`

Run this step again whenever you update your training images.

### Step 4: Run Face Recognition

```bash
python face_recognise.py
```

This script accesses the webcam, detects faces and identifies registered individuals using the trained model.

Unknown individuals are displayed as `unknown`.

Press `q` to exit.

### Step 5: Run Arduino-Based Access Control

1. Connect the Arduino board to your computer.
2. Open `ard_chaser/ard_chaser.ino` using Arduino IDE.
3. Select the appropriate Arduino board and COM port.
4. Upload the Arduino program.
5. Ensure the serial port is available and not being used by the Arduino Serial Monitor.
6. Check the Arduino COM port in Windows Device Manager.
7. Update the configured serial port in `face_recogniser1.py` if necessary.

Run the Arduino-integrated Python program:

```bash
python face_recogniser1.py
```

The system identifies individuals through the webcam and sends serial signals to the Arduino to control the LED based on authorization status.

Press `q` to exit.

## Expected Output

- Live webcam video feed.
- Detection of faces using Haar Cascade.
- Recognition of registered individuals.
- Identification of unknown faces.
- Arduino-controlled LED activation for an authorized individual.
- LED switched off when an authorized individual is not detected.

## Future Improvements

- Improve recognition accuracy under different lighting conditions.
- Add support for registering new users through an easier interface.
- Make hardware configuration more flexible.
- Develop a graphical user interface.
- Improve the overall system's usability and performance.

## Author

**Sharan Suresh**

GitHub: [https://github.com/sharanftww](https://github.com/sharanftww)

Project Repository: [Face Recognition-Based Access Control System](https://github.com/sharanftww/Face-Recognition-System)