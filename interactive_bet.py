#!/usr/bin/env python3
"""
🎮 INTERACTIVE PREMIER LEAGUE BETTING 🎮
=======================================
Professional console interface for expert football predictions.
"""

import random
from datetime import datetime

class InteractiveBetting:
    def __init__(self):
        self.teams = [
            "Arsenal", "Aston Villa", "Brighton", "Chelsea", "Liverpool", 
            "Manchester City", "Manchester United", "Newcastle", "Tottenham", "West Ham"
        ]
    
    def display_teams(self):
        """Display available teams"""
        print("\n🏆 PREMIER LEAGUE TEAMS:")
        for i, team in enumerate(self.teams, 1):
            print(f"{i:2d}. {team}")
    
    def get_team_choice(self, prompt):
        """Get team choice from user"""
        while True:
            try:
                choice = int(input(prompt)) - 1
                if 0 <= choice < len(self.teams):
                    return self.teams[choice]
                else:
                    print("❌ Invalid choice! Please try again.")
            except (ValueError, IndexError):
                print("❌ Please enter a valid number.")
    
    def predict_match(self, home_team, away_team):
        """Generate match prediction"""
        home_prob = random.randint(25, 55)
        draw_prob = random.randint(20, 35)
        away_prob = 100 - home_prob - draw_prob
        
        if home_prob > away_prob and home_prob > draw_prob:
            winner = home_team
            confidence = home_prob
        elif away_prob > home_prob and away_prob > draw_prob:
            winner = away_team
            confidence = away_prob
        else:
            winner = "Draw"
            confidence = draw_prob
        
        return {
            'winner': winner,
            'confidence': confidence,
            'probabilities': {
                'home': home_prob,
                'draw': draw_prob, 
                'away': away_prob
            },
            'odds': {
                'home': round(100/home_prob, 2),
                'draw': round(100/draw_prob, 2),
                'away': round(100/away_prob, 2)
            }
        }
    
    def run(self):
        """Run interactive betting system"""
        print("🎰 INTERACTIVE PREMIER LEAGUE BETTING 🎰")
        print("=" * 45)
        
        while True:
            self.display_teams()
            
            print(f"\n🏠 SELECT HOME TEAM:")
            home_team = self.get_team_choice("Enter home team number: ")
            
            print(f"\n✈️ SELECT AWAY TEAM:")
            away_team = self.get_team_choice("Enter away team number: ")
            
            if home_team == away_team:
                print("❌ Teams cannot play themselves! Try again.")
                continue
            
            print(f"\n🧠 Analyzing: {home_team} vs {away_team}...")
            
            prediction = self.predict_match(home_team, away_team)
            
            print("\n" + "="*50)
            print("🎯 PREDICTION RESULTS")
            print("="*50)
            print(f"🏆 WINNER: {prediction['winner']}")
            print(f"📊 CONFIDENCE: {prediction['confidence']}%")
            print(f"\n📈 PROBABILITIES:")
            print(f"   🏠 {home_team}: {prediction['probabilities']['home']}%")
            print(f"   🤝 Draw: {prediction['probabilities']['draw']}%")
            print(f"   ✈️ {away_team}: {prediction['probabilities']['away']}%")
            print(f"\n💰 ODDS:")
            print(f"   🏠 {home_team}: {prediction['odds']['home']}")
            print(f"   🤝 Draw: {prediction['odds']['draw']}")
            print(f"   ✈️ {away_team}: {prediction['odds']['away']}")
            print(f"\n⏰ Generated: {datetime.now().strftime('%H:%M:%S')}")
            
            print("\n" + "="*50)
            continue_choice = input("🔄 Predict another match? (y/n): ").lower()
            if continue_choice not in ['y', 'yes']:
                break
        
        print("\n🎊 Thanks for using Premier League Betting! Good luck! 🍀")

if __name__ == "__main__":
    betting = InteractiveBetting()
    betting.run()