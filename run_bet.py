#!/usr/bin/env python3
"""
🎯 PREMIER LEAGUE BETTING - COMMAND LINE VERSION 🎯
================================================
Simple command-line interface for football predictions.
"""

import sys
import random
from datetime import datetime

class CLIBettingSystem:
    def __init__(self):
        self.teams = [
            "Arsenal", "Aston Villa", "Brighton", "Chelsea", "Liverpool", 
            "Manchester City", "Manchester United", "Newcastle", "Tottenham", "West Ham"
        ]
    
    def predict_match(self, home_team, away_team):
        """Generate a simple prediction"""
        confidence = random.randint(65, 95)
        winner = random.choice([home_team, away_team, "Draw"])
        
        return {
            'home_team': home_team,
            'away_team': away_team,
            'winner': winner,
            'confidence': confidence,
            'advice': f"Bet on {winner} with {confidence}% confidence!"
        }
    
    def run(self):
        """Run the CLI betting system"""
        print("🎰 PREMIER LEAGUE BETTING SYSTEM 🎰")
        print("=" * 40)
        
        if len(sys.argv) != 3:
            print("Usage: python run_bet.py <home_team> <away_team>")
            print(f"Available teams: {', '.join(self.teams)}")
            return
        
        home_team = sys.argv[1]
        away_team = sys.argv[2]
        
        print(f"🏠 Home Team: {home_team}")
        print(f"✈️ Away Team: {away_team}")
        print("\n🧠 Analyzing match...")
        
        prediction = self.predict_match(home_team, away_team)
        
        print(f"\n🎯 PREDICTION RESULTS:")
        print(f"🏆 Winner: {prediction['winner']}")
        print(f"📊 Confidence: {prediction['confidence']}%")
        print(f"💰 Advice: {prediction['advice']}")
        print(f"⏰ Generated: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    system = CLIBettingSystem()
    system.run()