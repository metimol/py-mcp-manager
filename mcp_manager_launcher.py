#!/usr/bin/env python3
"""
Launcher script for MCP Manager that gracefully handles headless environments.
"""
import sys
import os


def print_headless_error(error_msg):
    """Print helpful error message for headless environments."""
    print("Error: Cannot start GUI application in headless environment.", file=sys.stderr)
    print("", file=sys.stderr)
    print("This application requires a graphical display. Solutions:", file=sys.stderr)
    print("", file=sys.stderr)
    print("1. Install and set up X11 forwarding:", file=sys.stderr)
    print("   # For SSH connections:", file=sys.stderr)
    print("   ssh -X your-server", file=sys.stderr)
    print("", file=sys.stderr)
    print("2. Use virtual display (Xvfb):", file=sys.stderr)
    print("   # Install xvfb:", file=sys.stderr)
    print("   sudo apt-get install xvfb  # On Ubuntu/Debian", file=sys.stderr)
    print("   # Run with virtual display:", file=sys.stderr)
    print("   xvfb-run -a python mcp_manager.py", file=sys.stderr)
    print("", file=sys.stderr)
    print("3. Use offscreen mode (no visible GUI):", file=sys.stderr)
    print("   QT_QPA_PLATFORM=offscreen python mcp_manager_launcher.py", file=sys.stderr)
    print("", file=sys.stderr)
    print("4. In Docker, ensure proper X11 setup:", file=sys.stderr)
    print("   # Linux:", file=sys.stderr)
    print("   docker run -it --rm \\", file=sys.stderr)
    print("     -e DISPLAY=$DISPLAY \\", file=sys.stderr)
    print("     -v /tmp/.X11-unix:/tmp/.X11-unix:rw \\", file=sys.stderr)
    print("     your-image", file=sys.stderr)
    print("", file=sys.stderr)
    print("   # macOS with XQuartz:", file=sys.stderr)
    print("   docker run -it --rm \\", file=sys.stderr)
    print("     -e DISPLAY=host.docker.internal:0 \\", file=sys.stderr)
    print("     your-image", file=sys.stderr)
    print("", file=sys.stderr)
    print("   # Or use offscreen mode in Docker:", file=sys.stderr)
    print("   docker run -it --rm \\", file=sys.stderr)
    print("     -e QT_QPA_PLATFORM=offscreen \\", file=sys.stderr)
    print("     your-image", file=sys.stderr)
    print("", file=sys.stderr)
    print("5. Update Dockerfile to include necessary packages:", file=sys.stderr)
    print("   RUN apt-get update && apt-get install -y \\", file=sys.stderr)
    print("       xvfb libxkbcommon-x11-0 libxcb-cursor0 \\", file=sys.stderr)
    print("       libegl-mesa0 && rm -rf /var/lib/apt/lists/*", file=sys.stderr)
    print("", file=sys.stderr)
    print(f"Technical details: {error_msg}", file=sys.stderr)


def main():
    """Main entry point that handles import errors gracefully."""
    try:
        # Try to import and run the main application
        from mcp_manager import main as mcp_main
        mcp_main()
    except ImportError as e:
        error_msg = str(e).lower()
        if any(keyword in error_msg for keyword in ['libegl', 'xcb', 'qt', 'display', 'platform']):
            print_headless_error(str(e))
            sys.exit(1)
        else:
            # Re-raise other import errors
            raise
    except SystemExit as e:
        # Handle normal sys.exit() calls from QApplication
        if e.code != 0:
            error_msg = str(e).lower()
            # Check if it's a Qt-related exit
            if hasattr(e, 'args') and e.args:
                error_msg = str(e.args[0]).lower()
            # For Qt platform plugin errors, the exit typically happens with code 1
            # but we won't catch those here as they're not SystemExit with specific messages
        raise
    except Exception as e:
        error_msg = str(e).lower()
        if any(keyword in error_msg for keyword in ['display', 'xcb', 'qt', 'platform', 'could not connect']):
            print_headless_error(str(e))
            sys.exit(1)
        else:
            # Re-raise other exceptions
            raise


if __name__ == "__main__":
    main()