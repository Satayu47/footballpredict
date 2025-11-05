#!/usr/bin/env python3
"""
🧪 SYSTEM TEST VERIFICATION 🧪
==============================
Complete test suite to verify all betting system components work perfectly.
"""

import requests
import json
import time
import sys

def test_web_server():
    """Test if web server is running"""
    try:
        response = requests.get("http://localhost:5000/api/teams", timeout=5)
        if response.status_code == 200:
            print("✅ Web server is running")
            data = response.json()
            print(f"✅ Teams API working - {data['count']} teams available")
            return True
        else:
            print(f"❌ Web server returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Web server connection failed: {e}")
        return False

def test_predictions():
    """Test prediction API"""
    try:
        test_data = {
            "home_team": "ARS",
            "away_team": "LIV"
        }
        
        response = requests.post(
            "http://localhost:5000/api/predict", 
            json=test_data,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                prediction = data['prediction']
                print("✅ Prediction API working")
                print(f"   🏆 Winner: {prediction['winner']}")
                print(f"   📊 Confidence: {prediction['confidence']}%")
                print(f"   🎯 Trust Score: {prediction['trust_score']}%")
                return True
            else:
                print(f"❌ Prediction failed: {data.get('message', 'Unknown error')}")
                return False
        else:
            print(f"❌ Prediction API returned status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Prediction API connection failed: {e}")
        return False

def test_standings():
    """Test standings API"""
    try:
        response = requests.get("http://localhost:5000/api/standings", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success' and len(data['standings']) > 0:
                print("✅ Standings API working")
                print(f"   🏆 Top team: {data['standings'][0]['team']['name']} ({data['standings'][0]['points']} pts)")
                return True
        print("❌ Standings API failed")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Standings API connection failed: {e}")
        return False

def test_fixtures():
    """Test fixtures API"""
    try:
        response = requests.get("http://localhost:5000/api/live-fixtures", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success' and len(data['fixtures']) > 0:
                print("✅ Fixtures API working")
                print(f"   ⚽ Next match: {data['fixtures'][0]['home']} vs {data['fixtures'][0]['away']}")
                return True
        print("❌ Fixtures API failed")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Fixtures API connection failed: {e}")
        return False

def main():
    """Run complete system test"""
    print("🧪 PREMIER LEAGUE BETTING SYSTEM - VERIFICATION TEST")
    print("=" * 55)
    print("⏳ Testing all components...\n")
    
    tests_passed = 0
    total_tests = 4
    
    # Test web server
    if test_web_server():
        tests_passed += 1
    
    # Wait a moment between tests
    time.sleep(1)
    
    # Test predictions
    if test_predictions():
        tests_passed += 1
    
    time.sleep(1)
    
    # Test standings
    if test_standings():
        tests_passed += 1
    
    time.sleep(1)
    
    # Test fixtures  
    if test_fixtures():
        tests_passed += 1
    
    print(f"\n" + "=" * 55)
    print(f"🎯 TEST RESULTS: {tests_passed}/{total_tests} PASSED")
    
    if tests_passed == total_tests:
        print("🎉 ALL TESTS PASSED! Your betting system is working perfectly!")
        print("🎰 System Status: FULLY OPERATIONAL")
        print("💰 Ready for live betting!")
        return 0
    else:
        print(f"⚠️ {total_tests - tests_passed} tests failed")
        print("🔧 System needs attention")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)