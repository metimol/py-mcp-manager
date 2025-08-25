# Heroku Deployment

This document explains how to deploy MCP Manager to Heroku using buildpacks.

## Important Note

⚠️ **MCP Manager is designed as a desktop application with a GUI interface.** The Heroku deployment provides a minimal web interface for compatibility but does not include the full functionality of the desktop application.

## Deployment

### Option 1: Deploy to Heroku with One Click

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Option 2: Manual Deployment

1. Clone the repository:
   ```bash
   git clone https://github.com/metimol/py-mcp-manager.git
   cd py-mcp-manager
   ```

2. Create a Heroku app:
   ```bash
   heroku create your-app-name
   ```

3. Deploy:
   ```bash
   git push heroku main
   ```

## What's Deployed

The Heroku deployment includes:

- **Web Server**: A minimal HTTP server (`web_server.py`) that serves an informational page
- **No GUI**: The PyQt6 desktop interface is not available in the Heroku environment
- **Documentation**: Information about downloading and using the full desktop application

## Files for Heroku Deployment

The following files enable Heroku buildpack compatibility:

- **`Procfile`**: Defines the web process (`web: python web_server.py`)
- **`runtime.txt`**: Specifies Python version (`python-3.12.7`)
- **`requirements.txt`**: Lists dependencies (none needed for web mode)
- **`web_server.py`**: Minimal web server for Heroku compatibility

## Environment Variables

The web server automatically uses the `PORT` environment variable provided by Heroku.

## Local Testing

Test the web interface locally:

```bash
# Start the web server
python web_server.py

# Or with a specific port
PORT=8080 python web_server.py
```

Visit `http://localhost:5000` (or your specified port) to see the web interface.

## Full Desktop Application

For complete functionality, install and run the desktop application locally:

```bash
# Install
pip install py-mcp-manager

# Run
mcp-manager
```

Or download from the [GitHub repository](https://github.com/metimol/py-mcp-manager).