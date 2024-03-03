# Use a lightweight Python image
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt
# Install necessary system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libsndfile1 \
        ffmpeg \
        espeak \
        alsa-utils \
        libasound2-dev \
        jackd2 \
        dbus-x11 \
	xvfb \
        gcc \
        libasound-dev \
        libportaudio2 \ 
        libportaudiocpp0 \ 
        portaudio19-dev \
        libc6-dev \
    && rm -rf /var/lib/apt/lists/*
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt --timeout=1500
# Set environment variable to use the host's /dev/snd
ENV PULSE_SERVER unix:/run/user/1000/pulse/native
Volume /dev/snd
# Set up XVFB and PulseAudio
ENV DISPLAY=:0.0
RUN Xvfb :0 -screen 0 1024x768x24 &
# RUN  jack_control start
# Command to run the Python script
CMD ["python", "speech.py"]
