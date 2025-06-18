# 🚀 Quick Start Guide – Face Recognition with AWS Rekognition

This guide will help you run the project in a few simple steps using AWS.

---

## 1️⃣ What You Need First

- An AWS account  
- A basic computer with terminal access  
- AWS CLI installed and configured (`aws configure`)  
- Python 3 installed on your EC2 instance

---

## 2️⃣ Launch an EC2 Instance (from AWS Console)

Go to [EC2 Dashboard](https://console.aws.amazon.com/ec2):

- Launch a t2.micro instance with Amazon Linux 2  
- Allow SSH (port 22) in your security group  
- Download your key pair (e.g., `my-key.pem`)  

---

## 3️⃣ Connect to EC2

In your terminal:

```bash
ssh -i "my-key.pem" ec2-user@your-ec2-ip

4️⃣ Install Python & Boto3 on EC2

sudo yum update -y
sudo yum install python3 -y
pip3 install boto3

---

## 5️⃣ Upload Images & Script
Transfer images from your local machine to EC2:

```bash
scp -i "my-key.pem" ./Human_Face_1.jpg ec2-user@your-ec2-ip:~/
Repeat for each image and also for the face_recognition.py script.

---

6️⃣ Upload Images to S3
On your EC2 instance:
```bash
aws s3 mb s3://your-bucket-name
aws s3 cp Human_Face_1.jpg s3://your-bucket-name/

---

7️⃣ Create Rekognition Collection
```bash
aws rekognition create-collection --collection-id my-face-collection

---

8️⃣ Run the Script!
```bash
python3 face_recognition.py

Choose:

upload to add images

identify to find matches

🧹 Done? Clean Up (Optional)
```bash
aws rekognition delete-collection --collection-id my-face-collection
aws s3 rb s3://your-bucket-name --force