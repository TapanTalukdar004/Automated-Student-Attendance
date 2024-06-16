# Automated Student Attendance System Using Python



## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [System Requirements](#system-requirements)
- [Future Work](#future-work)
- [Contributors](#contributors)
- [License](#license)

## Introduction
In the digital age, efficient management of classroom attendance is essential. This project aims to simplify and streamline the process of tracking student attendance using facial recognition technology. Developed with Python, OpenCV, and Streamlit, the system captures real-time images, recognizes faces from pre-stored photos, and records attendance data, addressing common issues associated with traditional methods like manual errors and time consumption.

## Features
- Real-time face detection and recognition
- Automated attendance marking
- Simple web interface for managing student data and capturing attendance
- Storage of attendance records in CSV files for easy retrieval and analysis

## Technologies Used
- **Python 3.x**: Core programming language
- **OpenCV**: For accessing the webcam and capturing real-time images
- **face_recognition**: For detecting and recognizing student faces
- **Streamlit**: For creating the web-based user interface
- **NumPy**: For numerical operations and handling arrays
- **Pandas**: For data manipulation and analysis
- **CSV**: For storing attendance records

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automated-attendance-system.git
    cd automated-attendance-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to the displayed URL (usually `http://localhost:8501`).

3. Use the sidebar to add student details and upload photos.

4. Start the attendance process and let the system capture and recognize faces in real-time.

## Screenshots
![Streamlit Interface](images/interface.png)  <!-- Replace with your actual screenshot path -->

![OpenCV Working](images/opencv_working.png)  <!-- Replace with your actual screenshot path -->

![CSV File](images/csv_file.png)  <!-- Replace with your actual screenshot path -->

## System Requirements
### Hardware Requirements
- **Computer with at least 4GB of RAM**: To handle data processing efficiently
- **Processor**: Intel Core i3 or equivalent for sufficient computational power
- **Storage**: Minimum 10GB of free space to store the dataset and related files

### Software Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python 3.x**: The programming language used for implementing the project
- **Libraries and Packages**:
  - NumPy: For numerical operations and handling arrays
  - Pandas: For data manipulation and analysis
  - face_recognition: For face detection and recognition
  - OpenCV: For real-time image capturing
  - Streamlit: For web interface
  - CSV: For data storage
- **IDE**: Visual Studio Code

## Future Work
Future work includes enhancing accuracy with advanced face recognition algorithms, developing a mobile app, integrating cloud storage, providing real-time alerts, and ensuring data encryption and compliance with privacy regulations.

## Contributors
- **Your Name** (yourusername) <!-- Replace with actual names and GitHub usernames -->
- **Team Member 1** (username)
- **Team Member 2** (username)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

