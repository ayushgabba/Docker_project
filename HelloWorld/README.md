# 🚀 Docker HelloWorld Project

## 📌 Description

A simple Docker project that runs a Python script inside a container. This project demonstrates how to create a lightweight Docker container using Python.

## 🛠 Features

✅ Uses Python 3.9 slim image\
✅ Minimal Dockerfile setup\
✅ Easy to build and run

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/downloads)

## 🚀 Getting Started

### Step 1: Create the Python Application ♻️

First, let's create a simple Python script that prints "Hello World".

1. Create a file named `app.py` and add the following code:

```python
# app.py
print("Hello World! 🌍")
```

### Step 2: Install Docker and Python 🛠️

1. Install Docker  
   Download and install Docker Desktop from the [official Docker website](https://www.docker.com/get-started). Once installed, start Docker Desktop and ensure it is running.

2. Install Python  
   Download and install Python from the [official Python website](https://www.python.org/downloads/).

### Step 3: Verify Installations ✅

Before proceeding, let's verify that Docker and Python are installed correctly.

#### Check Docker Version

Run the following command in your terminal:

```bash
docker --version
```

You should see an output similar to:

```
Docker version 20.10.12, build e91ed57
```

### Step 4: Clone the Repository 🌀

```bash
git clone https://github.com/ayushgabba/Docker_HelloWorld.git
cd Docker_HelloWorld
```

### Step 5: Build the Docker Image 🏗️

```bash
docker build -t hello-world-app .
```

### Step 6: Run the Container 🚀

```bash
docker run hello-world-app
```

## 📜 Code Overview

Below is the **Dockerfile** used in this project:

```dockerfile
# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app.py to the container
COPY . /app

# Run the Python script
CMD ["python", "app.py"]
```

## 📢 Expected Output

Once you run the container, you should see the following output:

```
Hello World! 🌍
```

