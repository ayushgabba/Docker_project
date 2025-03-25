# Deploying a Streamlit App on AWS EC2

This guide explains how to deploy a Streamlit application on an AWS EC2 instance and access it via a public IP.

## Prerequisites
- An AWS EC2 instance (Ubuntu 20.04 or later recommended)
- SSH access to the instance
- Docker installed on the instance
- Streamlit app code in a GitHub repository (optional)

## Steps to Deploy

### 1. Connect to EC2 Instance
```sh
ssh -i your-key.pem ubuntu@13.60.68.24
```

### 2. Install Docker (If Not Installed)
```sh
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

### 3. Clone Your Streamlit App (Optional)
If your Streamlit app is in a GitHub repository, clone it:
```sh
git clone https://github.com/your-repo/your-streamlit-app.git
cd your-streamlit-app
```

### 4. Create a Dockerfile
If you don’t already have a `Dockerfile`, create one:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 5. Build and Run Docker Container
```sh
sudo docker build -t streamlit-app .
sudo docker run -d -p 8501:8501 streamlit-app
```

### 6. Allow Traffic to Port 8501
Ensure your AWS security group allows inbound traffic on port 8501.

### 7. Access the Streamlit App
Visit:
```
http://13.60.68.24:8501/
```

## Troubleshooting
- Check logs: `sudo docker logs <container_id>`
- Restart container: `sudo docker restart <container_id>`
- Ensure port 8501 is open in AWS Security Groups

## Conclusion
You have successfully deployed a Streamlit app on AWS EC2 using Docker. 🎉

