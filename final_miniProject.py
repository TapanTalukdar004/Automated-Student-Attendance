import streamlit as st
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os


def mark_attendance(known_face_encodings, known_face_names, student_roll_numbers, csv_file_path):
    processed_faces = set()  

    video_capture = cv2.VideoCapture(0)

    
    with open(csv_file_path, 'a', newline='') as f:
        csv_writer = csv.writer(f)

        while True:
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                roll_number = "Unknown"

                for i, match in enumerate(matches):
                    if match:
                        name = known_face_names[i]
                        roll_number = student_roll_numbers[i]

                        
                        if (name, roll_number) not in processed_faces:
                            processed_faces.add((name, roll_number))  # Add name and roll number to set of processed faces
                            csv_writer.writerow([name, roll_number, datetime.now().strftime("%I:%M:%S %p"), "Present"])
                            st.success(f"{name} marked present")
                        
                        break

            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()


st.title("Student Attendance System")

# Sidebar for adding student details
st.sidebar.title("Add Student Details")

name = st.sidebar.text_input("Name", "")
roll_number = st.sidebar.text_input("Roll Number", "")
photo_upload = st.sidebar.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])
if st.sidebar.button("Add Student") and name and roll_number and photo_upload:
    # Save uploaded photo
    folder_path = "student_photos"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, f"{roll_number}_{name}.jpg")
    with open(file_path, "wb") as f:
        f.write(photo_upload.getvalue())

    st.sidebar.success(f"Photo uploaded for {name} with Roll No. {roll_number}")

# Main page for marking attendance
if st.button("Start Attendance"):
    if os.path.exists("student_photos") and os.listdir("student_photos"):
        known_face_encodings = []
        known_face_names = []
        student_roll_numbers = []

        # Load known faces, names, and roll numbers
        for file_name in os.listdir("student_photos"):
            image = face_recognition.load_image_file(os.path.join("student_photos", file_name))
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(file_name.split("_", 1)[1].split(".")[0])  # Extract name without roll number prefix
            
            # Extract roll number from file name
            roll_number = file_name.split("_")[0]  # Assuming roll number is the prefix before underscore in file name
            student_roll_numbers.append(roll_number)

        # Create or open CSV file
        current_date = datetime.now().strftime("%dth %B, %Y")
        csv_file_name = f"{current_date}.csv"
        csv_file_path = os.path.join(os.getcwd(), csv_file_name)
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(["Name", "Roll Number", "Time", "Status"])

        # Mark attendance
        mark_attendance(known_face_encodings, known_face_names, student_roll_numbers, csv_file_path)
        st.success("Attendance marked successfully")

    else:
        st.error("No student photos found. Please upload photos first.")
