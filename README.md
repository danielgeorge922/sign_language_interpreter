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
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
4. **Configure AWS and Google Cloud:**

Set up your AWS credentials and configuration files for accessing SageMaker and S3.

Obtain your Google Cloud API key and set it as an environment variable:

bash```
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/google-cloud-api-key.json"
```

Run the Flask server:

```bash
flask run --host=0.0.0.0 --port=5000
```
Frontend
Navigate to the frontend directory:

bash
Copy code
cd sign-language-translation-tool/frontend
Install frontend dependencies:

bash
Copy code
npm install
Run the React application:

bash
Copy code
npm start
Training the Model
The model was trained using AWS SageMaker, leveraging its powerful infrastructure to handle large datasets and intensive computations. The training data, consisting of sign language keypoints, was stored in an Amazon S3 bucket. The trained model was then downloaded and integrated into this project.

Google Text-to-Speech Integration
The application uses the Google Text-to-Speech API to convert the translated text into audible speech. This enhances the user experience by providing immediate auditory feedback for the detected sign language gestures.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements, bug fixes, or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

vbnet
Copy code

This README provides a comprehensive overview of the project, setup instructions, and key features, tailored for someone reviewing your resume.



![image](https://github.com/user-attachments/assets/2248e915-5124-45c2-979f-8367c75a5c7f)
