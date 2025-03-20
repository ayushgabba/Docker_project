# Machine Learning Model Deployment Using Docker 🐳🤖

In this project, we will deploy a **Machine Learning (ML) model** using **Docker**, a powerful platform for containerizing applications. Docker ensures that your ML model is portable, scalable, and independent of the underlying system. This guide will walk you through the process of containerizing an ML model, training it, and deploying it as a Dockerized application.

By the end of this tutorial, you will have a fully functional ML model running inside a Docker container, ready for inference or further development. 🚀

---

## Project Overview 📖

This project demonstrates how to containerize an ML model using Docker. The model is trained on a dataset (e.g., `mushrooms.csv`) and deployed as a Streamlit web application. The application allows users to interact with the model and visualize predictions in real-time.

---

## Documentation 📚

For more information, refer to the official documentation:

- [Docker Documentation](https://docs.docker.com/)
- [ML Model Using Docker](https://www.geeksforgeeks.org/how-to-use-docker-for-machine-learning/)
- [Machine Learning Models](https://www.geeksforgeeks.org/machine-learning-models/)

---

## Prerequisites 📋

Before we begin, ensure you have the following installed on your system:

1. **Docker**: A platform for developing, shipping, and running applications in containers.
2. **Python**: A programming language used to write the ML model and application.
3. **Streamlit**: A framework for building interactive web apps with Python.

---

## Installation and Setup 🛠️

### Step 1: Verify Docker and Python Installation

#### Check Docker Version
Run the following command in your terminal:
```bash
docker --version
```

You should see an output similar to:

```bash
Docker version 20.10.17, build 100c701
```

Check Python Version

Run the following command in your terminal:

```bash
python --version
```

You should see an output similar to:

```bash
Python 3.9.7
```

## Project Structure 🗂️

The project consists of the following files:

1. app.py: The main Python script containing the ML model and Streamlit application.
2. requirements.txt: A file listing all Python dependencies required for the project.
3. Dockerfile: A script containing instructions for Docker to build an image.
4. mushrooms.csv: The dataset used to train the ML model.

## Create the ML Model and Streamlit App 🐍

Step 1: Import the ML Model

The ML model is already available in the app.py file. This script includes the following:

Data preprocessing.
Model training.
Streamlit interface for user interaction.
Step 2: Create requirements.txt

Generate a requirements.txt file to list all Python dependencies:

```bash
pip freeze > requirements.txt
```
## Dockerfile 📄

The Dockerfile is a script that contains instructions for Docker to build an image. Below is the Dockerfile for this project:


```bash
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the working directory
COPY app.py /app
COPY requirements.txt /app
COPY mushrooms.csv /app

# Upgrade pip and install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Set the entrypoint command to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Explanation of the Dockerfile:

1. FROM python:3.9-slim: Specifies the base image (Python 3.9 slim).
2. WORKDIR /app: Sets the working directory inside the container.
3. COPY: Copies the application files (app.py, requirements.txt, and mushrooms.csv) to the container.
4. RUN: Upgrades pip and installs Python dependencies from requirements.txt.
5. EXPOSE 8501: Exposes port 8501 for the Streamlit app.
6. ENTRYPOINT: Specifies the command to run the Streamlit app.

## Deployment 🚀
Step 1: Build the Docker Image

Navigate to the directory containing the Dockerfile and run the following command:

```bash
docker build -t ml-model .
```

* The -t flag tags the image with the name ml-model.
* The . specifies the build context (current directory).


Step 2: Verify the Docker Image

Run the following command to list all Docker images:

```bash
docker images
```

You should see an output similar to:

```bash
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
ml-model     latest    abc123def456   10 seconds ago   1.02GB
```

Step 3: Run the Docker Container

Start the Docker container using the following command:

```bash
docker run -p 8501:8501 ml-model
# Deploying a Streamlit App on AWS EC2 🚀🌐

Welcome to **My App**! This project demonstrates how to deploy a **Streamlit application** on an **AWS EC2 instance** using **Docker**. The application serves as an interactive web interface for [brief description of your app, e.g., "analyzing and visualizing mushroom species data"]. By containerizing the app with Docker, we ensure portability, scalability, and ease of deployment.

This guide will walk you through the entire process, from setting up your EC2 instance to running the Streamlit app in a Docker container. By the end, you'll have a fully functional web application accessible from anywhere. 🌟

---

## Overview 📖

This project includes:
1. **Streamlit App**: A Python-based web application for interactive data visualization.
2. **Docker**: Used to containerize the app for seamless deployment.
3. **AWS EC2**: A cloud-based virtual server to host the application.

The app is designed to provide an engaging and user-friendly experience, allowing users to explore and interact with data in real-time.

---

## Features 🌟

- **Interactive UI**: Intuitive and responsive interface for seamless navigation.
- **Data Visualization**: Dynamic charts and graphs to analyze datasets.
- **Scalable Architecture**: Dockerized for easy deployment and scaling.
- **Cloud Hosting**: Hosted on AWS EC2 for global accessibility.

---

## Prerequisites 📋

Before you begin, ensure you have the following:

1. **AWS Account**: To create and manage EC2 instances.
2. **Amazon Linux 2 EC2 Instance**: A virtual server to host the application.
3. **Docker**: Installed on the EC2 instance for containerization.
4. **SSH Access**: To connect to the EC2 instance remotely.
5. **Basic Command Line Knowledge**: Familiarity with Linux commands and Docker.

---

## Step 1: Set Up Your AWS EC2 Instance 🖥️

### 1.1 Launch an EC2 Instance
1. Log in to your **AWS Management Console**.
2. Navigate to the **EC2 Dashboard** and click **Launch Instance**.
3. Choose **Amazon Linux 2 AMI** as the operating system.
4. Select an instance type (e.g., `t2.micro` for free tier).
5. Configure security groups to allow SSH (port 22) and HTTP (port 8501) traffic.
6. Launch the instance and download the key pair (`.pem` file).

### 1.2 Connect to the EC2 Instance
Use the following command to connect to your EC2 instance via SSH:
```bash
ssh -i /path/to/your-key.pem ec2-user@your-ec2-public-ip
```

## Step 2: Install Docker on EC2 🐳

2.1 Update the System

Ensure your system is up to date:

```bash
sudo yum update -y
```
2.2 Install Docker

Install Docker using the following commands:

```bash
sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
```
Restart your SSH session for the changes to take effect.

2.3 Verify Docker Installation

Check if Docker is installed and running:

```bash
docker --version
sudo service docker status
```

## Step 3: Deploy the Streamlit App 🚀

3.1 Clone the Repository

Clone the repository containing the Streamlit app:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

3.2 Build the Docker Image

Build the Docker image for the Streamlit app:

```bash
docker build -t streamlit-app .
```

3.3 Run the Docker Container

Start the Docker container and map port 8501:
```bash
docker run -d -p 8501:8501 --name my-streamlit-app streamlit-app
```
## Step 4: Access the Streamlit App 🌐

1. Open your web browser and navigate to:

```bash
http://<your-ec2-public-ip>:8501
```
2. You should see the Streamlit app running.

## Step 5: Automate Deployment (Optional) 🤖

To ensure the app runs automatically after a system reboot, use the following command:

```bash
sudo docker update --restart unless-stopped my-streamlit-app
```

## Troubleshooting 🛠️

Issue: Cannot Access the App

Ensure the security group allows inbound traffic on port 8501.
Verify the Docker container is running:

```bash
docker ps
```
Issue: Docker Permission Denied

Add your user to the Docker group:
```bash
sudo usermod -a -G docker ec2-user
```

## Conclusion 🎉

Congratulations! 🎉 You’ve successfully deployed a Streamlit app on an AWS EC2 instance using Docker. This setup ensures your application is scalable, portable, and accessible from anywhere. Whether you're building data visualization tools, machine learning dashboards, or interactive web apps, this deployment strategy provides a robust foundation for your projects.

Keep exploring and building amazing applications with Streamlit, Docker, and AWS! 🚀🐳

Happy coding! 💻✨