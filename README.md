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
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)

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

Installation instructions will be added after verifying the required Python libraries and project dependencies.

## Execution

Execution instructions will be added after verifying the correct order of running the Python scripts and Arduino program.

## Expected Output

- Live webcam feed.
- Detection of faces in the camera frame.
- Recognition of registered individuals.
- Identification of unknown faces.
- LED indication through Arduino integration.

## Screenshots

Screenshots of the working application will be added here.

## Future Improvements

- Improve recognition accuracy under different lighting conditions.
- Add support for registering new users through an easier interface.
- Make hardware configuration more flexible.
- Develop a graphical user interface.
- Improve the overall system's usability and performance.

## Author

**Sharan Suresh**

GitHub: https://github.com/sharanftww