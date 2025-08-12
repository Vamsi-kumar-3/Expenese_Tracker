#!/usr/bin/env python3
"""
Development runner for the Flask Expense Tracker application.
This file provides an easy way to run the application in development mode.
"""

import os

# Try to load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, environment variables will be read from system
    pass

if __name__ == '__main__':
    from app import app
    
    # Get configuration from environment variables
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting Expense Tracker on {host}:{port}")
    print(f"Debug mode: {debug}")
    print("Press Ctrl+C to quit")
    
    app.run(host=host, port=port, debug=debug)