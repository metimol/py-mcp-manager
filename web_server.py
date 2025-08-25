#!/usr/bin/env python3
"""
Web server entry point for MCP Manager.
This provides a minimal web interface for Heroku deployment compatibility.
"""

import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler


class MCPManagerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>MCP Manager</title>
            <style>
                body { 
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; 
                    margin: 0; 
                    padding: 40px; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                }
                .container { 
                    max-width: 800px; 
                    margin: 0 auto; 
                    background: white;
                    border-radius: 12px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                    overflow: hidden;
                }
                .header {
                    background: #2c3e50;
                    color: white;
                    padding: 30px;
                    text-align: center;
                }
                .content {
                    padding: 30px;
                }
                .info { 
                    background: #f8f9fa; 
                    padding: 20px; 
                    border-radius: 8px; 
                    margin: 20px 0; 
                    border-left: 4px solid #667eea;
                }
                .warning {
                    background: #fff3cd;
                    border-left: 4px solid #ffc107;
                    padding: 15px;
                    margin: 20px 0;
                    border-radius: 4px;
                }
                code {
                    background: #f1f3f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
                }
                ul {
                    line-height: 1.6;
                }
                a {
                    color: #667eea;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                .footer {
                    text-align: center;
                    padding: 20px;
                    background: #f8f9fa;
                    color: #6c757d;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🖥️ MCP Manager</h1>
                    <p>Model Context Protocol Server Manager</p>
                </div>
                <div class="content">
                    <div class="warning">
                        <strong>⚠️ Web Mode Active</strong><br>
                        This is a minimal web interface provided for Heroku deployment compatibility.
                        MCP Manager is designed as a desktop application with full GUI functionality.
                    </div>
                    
                    <div class="info">
                        <h3>📥 Get the Desktop Application</h3>
                        <p>For full functionality, install and run the desktop version:</p>
                        <ul>
                            <li><a href="https://github.com/metimol/py-mcp-manager" target="_blank">📁 GitHub Repository</a></li>
                            <li>📦 Install: <code>pip install py-mcp-manager</code></li>
                            <li>🚀 Run: <code>mcp-manager</code></li>
                        </ul>
                    </div>
                    
                    <div class="info">
                        <h3>✨ Desktop Features</h3>
                        <ul>
                            <li>🎛️ Graphical interface for managing MCP servers</li>
                            <li>▶️ Start, stop, and monitor server processes</li>
                            <li>⚙️ Configuration management with JSON export/import</li>
                            <li>📋 Real-time log viewing and monitoring</li>
                            <li>🌍 Environment variable management</li>
                            <li>📱 Cross-platform support (Windows, macOS, Linux)</li>
                        </ul>
                    </div>
                    
                    <div class="info">
                        <h3>🔧 About MCP</h3>
                        <p>The Model Context Protocol (MCP) enables secure connections between AI applications and data sources. MCP Manager simplifies the process of configuring and managing multiple MCP servers from a single interface.</p>
                    </div>
                </div>
                <div class="footer">
                    <p>MCP Manager v0.1.0 | Running in Web Mode</p>
                </div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        """Override to customize log format"""
        print(f"[{self.address_string()}] {format % args}")


def main():
    """Start the web server"""
    port = int(os.environ.get('PORT', 5000))
    
    print("🚀 Starting MCP Manager Web Server")
    print(f"🌐 Port: {port}")
    print("📝 This is a minimal web interface for deployment compatibility")
    print("💡 For full functionality, use the desktop application")
    print("─" * 50)
    
    server = HTTPServer(('0.0.0.0', port), MCPManagerHandler)
    
    try:
        print(f"✅ Server running at http://0.0.0.0:{port}")
        print("Press Ctrl+C to stop")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        server.server_close()
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()