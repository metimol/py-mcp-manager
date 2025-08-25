# MCP Manager

A desktop application for managing Model Context Protocol (MCP) servers with a graphical interface.

![MCP Manager Screenshot](assets/screenshot.png)

## Overview

MCP Manager simplifies the process of configuring, starting, stopping, and monitoring multiple MCP servers from a single interface.

## Installation

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

### Using uv (recommended)

```bash
# Clone the repository
git clone https://github.com/metimol/py-mcp-manager.git
cd py-mcp-manager

# Install dependencies
make install

# Run the application
make run
```

To create a standalone executable:

```bash
# Create macOS .app bundle
make package

# Install to Applications folder
make install-macosx
```

### Using Docker

You can also run MCP Manager using Docker:

```bash
# Pull the latest image from GitHub Container Registry
docker pull ghcr.io/metimol/py-mcp-manager:latest

# Run with X11 forwarding (Linux)
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v $HOME/.Xauthority:/home/app/.Xauthority:ro \
  ghcr.io/metimol/py-mcp-manager:latest

# Run with X11 forwarding (macOS with XQuartz)
# First install XQuartz and run: xhost +localhost
docker run -it --rm \
  -e DISPLAY=host.docker.internal:0 \
  ghcr.io/metimol/py-mcp-manager:latest
```

**Build from source:**

```bash
# Build the Docker image
docker build -t py-mcp-manager .

# Run the locally built image
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  py-mcp-manager
```

**Note:** Running GUI applications in Docker requires X11 forwarding or similar display mechanisms. The exact setup depends on your host operating system.

## Usage

1. Launch the application using one of the methods above
2. Click "+ Add Server" to create your first server configuration
3. Fill in the server details:
   - Server ID (unique identifier)
   - Display Name
   - Command to run the server
   - Arguments
   - Environment variables
   - Working directory
4. Click "Save"
5. Use the "Start" button to launch your server
6. Monitor logs and status in real-time

## Configuration

Server configurations are stored in a platform-appropriate user data directory:

- **macOS**: `~/Library/Application Support/MCP Manager/mcp_servers.json`
- **Windows**: `%APPDATA%\MCP Manager\mcp_servers.json`
- **Linux**: `~/.local/share/mcp-manager/mcp_servers.json`

You can:

- Manually edit this file when the application is not running
- Use the built-in JSON editor (View JSON button)
- Import/export configurations using the JSON import/export features

## License

This project is licensed under the MIT License - see the LICENSE file for details.
