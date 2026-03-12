# Raspberry-Pi-SPJ-VIT

Computer Vision project for **human detection and entry/exit counting** using a **Raspberry Pi**.
The system processes images, videos, and live camera feeds to detect people and count them when they cross a virtual line.

## Project Overview

This project is part of  Computer Vision and the goal is to build a lightweight system that can run on a Raspberry Pi and automatically count the number of people entering and exiting an area.

## Tools & Technologies

* Python
* OpenCV
* NumPy
* Raspberry Pi
* Camera

## Learning Stages

### 1. Image Processing

* Read and display images
* Convert to grayscale
* Resize / rotate images
* Edge detection
* Thresholding

### 2. Object Detection

* Bounding boxes for detected people
* Human detection using OpenCV / lightweight models

### 3. Video Processing

* Read video files
* Apply detection on each frame
* Display processed frames

### 4. Real-Time Camera Detection

* Capture live frames
* Detect humans in real time

### 5. People Counting

* Track detected people
* Detect line crossing direction
* Update entry and exit counters
  

## Basic Pipeline

Camera → Frame Capture → Human Detection → Tracking → Line Crossing Logic → Entry/Exit Counter
