# Rock Paper Scissors Game

## 🔹 Overview
- This is a Python-based **Rock, Paper, Scissors** game.
- User plays against the computer.
- You can choose how many rounds to play.
- After each round, scores are updated and shown.
- At the end, the overall winner is displayed.

## 🔹 Game Flow
1. Start the game from the menu  
2. Enter number of rounds  
3. For each round:
   - User selects Rock / Paper / Scissors  
   - Computer picks a random choice  
   - Winner is decided  
   - Scores are displayed  
4. After all rounds → final result shown

## 🔹 Rules
- Rock beats Scissors  
- Paper beats Rock  
- Scissors beat Paper  
- Same choices → Tie

## 🔹 Functions Used
- `get_user_choice()` → gets user input  
- `get_computer_choice()` → generates computer's move  
- `determiner()` → decides round winner and updates score  
- `overall_winner()` → prints final winner  
