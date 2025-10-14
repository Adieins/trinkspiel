FROM python:3.10-slim-bullseye

# Systemabhängigkeiten
RUN apt-get update && apt-get install -y \
    git openjdk-17-jdk unzip wget libncurses5 build-essential python3-pip \
    && pip install --upgrade pip \
    && pip install buildozer cython virtualenv \
    && rm -rf /var/lib/apt/lists/*

# Android SDK Commandline Tools
ENV ANDROID_SDK_ROOT=/opt/android-sdk
RUN mkdir -p $ANDROID_SDK_ROOT/cmdline-tools \
    && cd $ANDROID_SDK_ROOT/cmdline-tools \
    && wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O cmdline-tools.zip \
    && unzip cmdline-tools.zip \
    && rm cmdline-tools.zip

# Build-Tools installieren
RUN yes | $ANDROID_SDK_ROOT/cmdline-tools/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT "build-tools;36.1.0" "platforms;android-36" "platform-tools"

# User anlegen
RUN useradd -ms /bin/bash kivyuser
USER kivyuser

WORKDIR /src