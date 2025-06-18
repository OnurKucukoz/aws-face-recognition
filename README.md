# Amazon Rekognition Face Recognition System

This project demonstrates a simple yet powerful face recognition system using **Amazon Rekognition**, hosted on AWS services like **S3**, **EC2**, and **AWS CLI**.

## 📌 Project Features

- Upload images to S3 and index them using Rekognition's face collection.
- Identify and match new images against the indexed faces.
- Uses Boto3 for interacting with AWS Rekognition from a Python script.
- Easily extendable for employee tracking, access control, or VIP recognition systems.

## 🧰 Technologies & Services Used

- Amazon Rekognition  
- Amazon S3  
- Amazon EC2  
- AWS CLI  
- Python 3 & Boto3  

## 🚀 Setup Instructions

> Detailed setup steps are available in the `setup-instructions.md` file.

1. Launch an EC2 instance and connect via SSH.  
2. Install Python and Boto3.  
3. Configure AWS CLI.  
4. Upload your images to S3.  
5. Run the script: `python3 face_recognition.py`  
6. Choose `upload` to add faces or `identify` to match a face.  

## 🧠 How It Works

- The script uses **Rekognition’s IndexFaces** API to store facial features.  
- Later, it uses **SearchFacesByImage** to compare new images with existing ones.  
- Everything is stored and referenced from your S3 bucket.

## 📂 Project Structure
├── face_recognition.py # Main script<br>
├── README.md # Project documentation<br>
└── setup-instructions.md # Step-by-step deployment guide <br>
## 📸 Demo



## 📜 License

This project is open source and available under the MIT License.
