# Dockerfile README

This Dockerfile provides a setup for an application that asks yes or no questions, logs the conversation, and saves it into a log file.

## Instructions

### Building the Docker Image

To build the Docker image, follow these steps:

1. Ensure that Docker is installed on your system. If not, you can download and install it from [Docker's official website](https://docs.docker.com/get-docker/). Make sure that the time on the host machine is also synced.


2. Navigate to the directory containing the Dockerfile.

3. Open a terminal or command prompt and run the following command to build the Docker image:

    ```bash
    docker build -t nlpbot .
    ```

    Replace `nlpbot` with the desired name for your Docker image.

### Running the Docker Container

Once the Docker image is built, you can run a container using the following command:

```bash
docker run -it --device=/dev/snd:/dev/snd  -e PULSE_SERVER=unix:/run/user/1000/pulse/native  < image name > python speech.py

Concersations are logged in conversation_log.txt

