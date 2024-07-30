# Sign Language Translation Tool

## Overview

The Sign Language Translation Tool is a web application that translates sign language gestures into text and speech in real-time. This project integrates computer vision, machine learning, and real-time communication technologies to facilitate seamless interaction for individuals using sign language.

![Screenshot](path/to/screenshot.png)

## Features

- **Real-time Sign Detection**: Utilizes MediaPipe for detecting hand landmarks in real-time from webcam input.
- **Sign Language Translation**: Converts detected sign language gestures into corresponding text.
- **Text-to-Speech**: Uses Google Text-to-Speech API to convert the translated text into speech.
- **Word Construction**: Accumulates detected signs held for 2 seconds or more into full words for improved accuracy.

## Architecture

### Backend

- **Flask**: Serves as the backend framework.
- **Flask-SocketIO**: Handles real-time communication between the backend and frontend.
- **AWS SageMaker**: Utilized for training the machine learning model on sign language keypoints.
- **Amazon S3**: Stores training data and model artifacts.
- **MediaPipe**: Used for real-time hand landmark detection.
- **TensorFlow**: Framework for training and running the machine learning model.

### Frontend

- **React**: The frontend framework.
- **socket.io-client**: Facilitates real-time communication with the backend.
- **Video Feed Component**: Displays webcam feed and real-time detection results.

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js and npm
- AWS Account with SageMaker and S3 setup
- Google Cloud Platform account for Text-to-Speech API

### Setup Instructions

#### Backend

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/sign-language-translation-tool.git
   cd sign-language-translation-tool

2. **Set up a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

![image](https://github.com/user-attachments/assets/2248e915-5124-45c2-979f-8367c75a5c7f)
