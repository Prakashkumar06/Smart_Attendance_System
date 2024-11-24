Project Name: Face Recognition Attendance System

Description:

This Python script captures video frames from a webcam, detects faces using Haar cascades, recognizes them using a K-Nearest Neighbors (KNN) classifier, and marks attendance in a CSV file. It also includes text-to-speech functionality to announce attendance.

Instructions:

Install Libraries: Ensure you have the necessary libraries installed: OpenCV (cv2), pickle (pickle), NumPy (numpy), os (os), time (time), datetime (datetime), KNeighborsClassifier (sklearn.neighbors.KNeighborsClassifier), and optionally, win32com for text-to-speech (win32com.client).

Prepare Training Data:

Create a Data folder in your project directory.
Train the KNN classifier with face images and corresponding labels beforehand. You can find tutorials online for face data collection and KNN training.
Save the trained data as pickle files: names.pkl (containing labels) and faces_data.pkl (containing face data).
Run the Script:

Open a terminal or command prompt in your project directory.
Run the script using python your_script_name.py.
How it Works:

Capture Video Frames: The script uses OpenCV to capture video frames from your webcam.

Face Detection: It converts frames to grayscale and uses the Haar cascade classifier (haarcascade_frontalface_default.xml) to detect faces.

Face Recognition:

Detected faces are cropped and resized.
The KNN classifier loaded from names.pkl and faces_data.pkl predicts the identity of each face.
Attendance Marking:

The script checks if a CSV file exists for the current date (e.g., Attendance_2024-11-25.csv).
If the file exists, the predicted name and timestamp are appended.
If the file doesn't exist, it's created with column names (NAME, TIME) and the first attendance record is written.
Text-to-Speech (Optional):

If the win32com library is installed, the script announces attendance using text-to-speech upon pressing 'o'.
Keyboard Controls:

'q': Quit the program.
'o': (Optional) Announce attendance and save it to the CSV file.

