from flask import Flask, request, jsonify
import json
import datetime
import os
import platform
import psutil
import requests
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Store command history
command_history = []

@app.route('/api/receive', methods=['POST'])
def receive_data():
    data = request.json or {}
    command = data.get('message', '').strip()
    
    # Add to command history
    command_history.append({
        'command': command,
        'timestamp': datetime.datetime.now().isoformat()
    })
    
    # Process the command
    response = process_jarvis_command(command)
    
    print(f"Received command: {command}")
    print(f"Response: {response}")
    
    return jsonify({
        "status": "success", 
        "received": data,
        "response": response,
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get system status and JARVIS information"""
    return jsonify({
        "status": "online",
        "system": {
            "platform": platform.system(),
            "python_version": platform.python_version(),
            "cpu_usage": psutil.cpu_percent(),
            "memory_usage": psutil.virtual_memory().percent,
            "uptime": get_uptime()
        },
        "jarvis": {
            "version": "1.0.0",
            "commands_processed": len(command_history),
            "last_command": command_history[-1]['command'] if command_history else None
        }
    })

@app.route('/api/commands', methods=['GET'])
def get_commands():
    """Get command history"""
    return jsonify({
        "commands": command_history[-10:],  # Last 10 commands
        "total": len(command_history)
    })

@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear command history"""
    global command_history
    command_history = []
    return jsonify({"status": "success", "message": "Command history cleared"})

def process_jarvis_command(command):
    """Process JARVIS commands and return appropriate responses"""
    command_lower = command.lower()
    
    # Time and date commands
    if any(word in command_lower for word in ['time', 'clock', 'hour']):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"🕐 The current time is {current_time}"
    
    if any(word in command_lower for word in ['date', 'day', 'today']):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"📅 Today is {current_date}"
    
    # System status commands
    if any(word in command_lower for word in ['status', 'system', 'health']):
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        return f"💻 System Status:\n• CPU Usage: {cpu_usage}%\n• Memory Usage: {memory_usage}%\n• Platform: {platform.system()}"
    
    # Greeting commands
    if any(word in command_lower for word in ['hello', 'hi', 'hey', 'greetings']):
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        return f"👋 {greeting}! I'm JARVIS, your AI assistant. How can I help you today?"
    
    # Help commands
    if any(word in command_lower for word in ['help', 'commands', 'what can you do']):
        return """🤖 I can help you with:
• Time and date information
• System status and health
• Weather information (coming soon)
• Web searches (coming soon)
• File operations (coming soon)
• And much more!

Just ask me anything!"""
    
    # Weather commands (placeholder)
    if any(word in command_lower for word in ['weather', 'temperature', 'forecast']):
        return "🌤️ Weather functionality is coming soon! I'll be able to check weather for any location."
    
    # Web search commands (placeholder)
    if any(word in command_lower for word in ['search', 'google', 'find']):
        return "🔍 Web search functionality is coming soon! I'll be able to search the internet for you."
    
    # File operations (placeholder)
    if any(word in command_lower for word in ['file', 'folder', 'directory']):
        return "📁 File operations are coming soon! I'll be able to help you manage files and folders."
    
    # Unknown commands
    return f"🤔 I received your command: '{command}'. I'm still learning and will add more capabilities soon. Try asking for 'help' to see what I can do!"

def get_uptime():
    """Get system uptime"""
    try:
        uptime_seconds = time.time() - psutil.boot_time()
        hours = int(uptime_seconds // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        return f"{hours}h {minutes}m"
    except:
        return "Unknown"

if __name__ == '__main__':
    print("🤖 JARVIS Backend Starting...")
    print("📍 API Endpoint: http://localhost:5000")
    print("🔗 Public URL: https://ec2e-2409-40d7-9-5e9d-2128-faea-ef5-a77b.ngrok-free.app")
    print("📡 Ready to receive commands!")
    app.run(host='0.0.0.0', port=5000, debug=True)
