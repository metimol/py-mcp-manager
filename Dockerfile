FROM python:3.12-slim

# Install system dependencies for PyQt6
RUN apt-get update && apt-get install -y \
    libqt6core6 \
    libqt6gui6 \
    libqt6widgets6 \
    libgl1-mesa-dri \
    libxkbcommon-x11-0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    libegl1 \
    libegl-mesa0 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN useradd --create-home --shell /bin/bash app

# Set working directory
WORKDIR /app

# Copy application source code
COPY --chown=app:app . .

# Install Python dependencies
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org \
    "pyqt6>=6.7.1"

# Switch to app user
USER app

# Set display environment variable (can be overridden)
ENV DISPLAY=:0

# Set entrypoint to use the launcher script
ENTRYPOINT ["python", "mcp_manager_launcher.py"]