# JARVIS Backend

An intelligent AI assistant backend built with Python Flask that processes natural language commands and provides intelligent responses.

## Features

- 🤖 **Intelligent Command Processing** - Understands natural language commands
- ⏰ **Time & Date** - Get current time and date information
- 💻 **System Status** - Monitor CPU, memory, and system health
- 👋 **Smart Greetings** - Context-aware greetings based on time of day
- 📝 **Command History** - Track all processed commands
- 🔧 **Multiple API Endpoints** - Status, commands, and management endpoints

## API Endpoints

### Main Command Endpoint
```
POST /api/receive
Content-Type: application/json

{
  "message": "What time is it?"
}
```

### System Status
```
GET /api/status
```

### Command History
```
GET /api/commands
```

### Clear History
```
POST /api/clear
```

## Example Commands

- `"What time is it?"` - Get current time
- `"What's today's date?"` - Get current date
- `"Hello JARVIS"` - Get greeting
- `"System status"` - Get system health
- `"Help"` - Show available commands

## Deployment

This backend is designed to be deployed on Render, Railway, or any cloud platform that supports Python Flask applications.

## Technologies

- Python 3.12
- Flask
- Flask-CORS
- psutil
- gunicorn 