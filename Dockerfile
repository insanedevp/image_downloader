# Use the official Python image based on Debian Bullseye for comprehensive package support
FROM python:3.9-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies, including libsystemd-dev and other required libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    swig \
    libassuan-dev \
    libdbus-1-dev \
    libdbus-glib-1-dev \
    libgpgme11-dev \
    libsystemd-dev \
    dbus \
    dbus-x11 \
    gnupg \
    build-essential \
    gettext \
    pkg-config \
    meson \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install wheel
RUN pip install --upgrade pip wheel

# Set the working directory
WORKDIR /app

# Copy the wheelhouse directory with pre-downloaded packages
COPY wheelhouse /wheelhouse

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies using the local wheelhouse
RUN pip install --no-cache-dir --find-links=/wheelhouse -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port the FastAPI app will use
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
