# Voice-Controlled Game

## Description
This is a simple voice-controlled game built with Python and Pygame. The player moves a character on the screen using voice commands such as "left", "right", "up", and "down". The goal is to avoid or interact with an enemy that moves towards the player. The game also keeps track of the player's score based on interactions.

## Features
- Voice commands for movement.
- Enemy that moves towards the player.
- Score tracking system.
- Real-time speech recognition using the `speech_recognition` library.

## Requirements
- Python 3.x
- `pygame` library
- `speech_recognition` library
- `pyaudio` library (for microphone input)

## Installation
1. Install the required dependencies:
   ```sh
   pip install pygame speechrecognition pyaudio
   ```
2. Run the script:
   ```sh
   python voice_controlled_game.py
   ```

## How to Play
- Speak the commands: "left", "right", "up", or "down" to move the character.
- The enemy moves towards the character.
- If the enemy reaches the character, the score increases and the enemy respawns.
- The game runs in a loop until manually closed.

## Controls
- **Voice Commands:**
  - Say **"left"** → Move character left
  - Say **"right"** → Move character right
  - Say **"up"** → Move character up
  - Say **"down"** → Move character down

## Future Improvements
- Add more game mechanics such as obstacles and power-ups.
- Enhance speech recognition for better accuracy.
- Implement different difficulty levels.

## Author
Developed as part of an AI-powered game experiment.
