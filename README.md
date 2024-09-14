This repository contains a Python project that performs real-time face recognition on a video file by comparing each frame with a reference image. The code detects the presence of a specific person in the video and logs various events, such as face detection time, similarity check time, and timestamps of matched faces. It also highlights faces in the video frames for visual inspection.

# Project Overview
This project allows users to:

Compare a reference image to each frame of a video to detect whether the reference face appears in the video.
Draw rectangles around detected faces (green for matched faces, red for unmatched).
Log timestamps where matches are detected.
Track the performance of face detection and matching across frames.

# Features
Face Recognition: Compares faces in a video with a reference image using face encoding and matching.
Performance Logging: Logs processing time for face detection, comparison, and overall frame processing.
Face Highlighting: Draws bounding boxes around matched and unmatched faces.
Match Timestamps: Saves timestamps where the face is detected in the video to a file.
Detailed Logs: Provides a log file with frame-by-frame details on processing times and results.

# Requirements
To run this project, ensure you have the following installed:

Python 3.x

OpenCV

face_recognition

All required Python libraries are listed in the requirements.txt file.

# Installation
### 1. Clone the Repository:

git clone git@github.com:imortezamosavi/Face-Recognition.git

cd Face-Recognition

### 2. Install Dependencies:

pip install -r requirements.txt

# Usage
To use the code, follow these steps:

### 1. Prepare Your Reference Image:

Place the reference image of the face you want to detect in the root directory (or any directory of your choice).
In the script, update the path to the reference image (for example, path/to/reference_image.jpg).

### 2. Prepare the Video File:

Place the video file you want to process in the root directory (or any directory of your choice).
In the script, update the path to the video file (for example, path/to/video_file.mp4).

### 3. Run the Script:

Once the reference image and video paths are set,run the script:

python face_recognition_video.py

### 4. View Results:

The video frames with highlighted faces (green or red rectangles) will be displayed in a window.
The timestamps of face matches will be saved in detected_timestamps.txt.
The performance and detailed event logs will be saved in face_recognition_log.txt.
