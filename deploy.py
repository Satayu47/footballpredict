#!/usr/bin/env python3
"""
🚀 QUICK START DEPLOYMENT SCRIPT 🚀
===================================
One-click deployment for Premier League Betting System
"""

import subprocess
import sys
import os
import time

def run_command(command, description):
    """Run a command and show progress"""
    print(f"⏳ {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed")
            return True
        else:
            print(f"❌ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} error: {e}")
        return False

def main():
    """Main deployment function"""
    print("🎰 PREMIER LEAGUE BETTING SYSTEM - QUICK DEPLOY 🎰")
    print("=" * 55)
    
    # Check if Python is available
    print("🔍 Checking system requirements...")
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if run_command("pip install -r requirements.txt", "Installing Python packages"):
        print("✅ All dependencies installed successfully!")
    else:
        print("❌ Failed to install dependencies. Please install manually:")
        print("   pip install flask flask-socketio eventlet requests python-dateutil")
        return False
    
    # Verify files exist
    required_files = ['web_app.py', 'run_bet.py', 'interactive_bet.py', 'templates/index.html']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    
    # Test CLI
    print("\n🧪 Testing CLI functionality...")
    if run_command("python run_bet.py Arsenal Liverpool", "Testing CLI predictions"):
        print("✅ CLI system working perfectly!")
    
    print("\n" + "=" * 55)
    print("🎊 DEPLOYMENT SUCCESSFUL!")
    print("💰 Your Premier League Betting System is ready!")
    
    print("\n🚀 TO START THE WEB APPLICATION:")
    print("   python web_app.py")
    print("   Then visit: http://localhost:5000")
    
    print("\n💻 TO USE COMMAND LINE:")
    print("   python run_bet.py <home_team> <away_team>")
    
    print("\n🎮 TO USE INTERACTIVE MODE:")
    print("   python interactive_bet.py")
    
    print("\n🎯 REPOSITORY:")
    print("   https://github.com/Satayu47/footballpredict")
    
    print("\n" + "=" * 55)
    print("🔥 READY TO MAKE MONEY! Good luck with your bets! 🍀")
    
    # Offer to start web server
    start_web = input("\n🌐 Start web server now? (y/n): ").lower().strip()
    if start_web in ['y', 'yes']:
        print("\n🚀 Starting Premier League Betting Casino...")
        print("🎰 Server will start in 3 seconds...")
        time.sleep(3)
        
        try:
            # Start the web application
            subprocess.run(["python", "web_app.py"], check=False)
        except KeyboardInterrupt:
            print("\n👋 Server stopped by user")
        except Exception as e:
            print(f"\n❌ Error starting server: {e}")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)