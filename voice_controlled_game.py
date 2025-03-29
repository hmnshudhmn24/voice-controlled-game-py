import pygame
import speech_recognition as sr
import threading
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Voice-Controlled Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Character settings
character_size = 50
character_x, character_y = WIDTH // 2, HEIGHT // 2
character_speed = 20

# Enemy settings
enemy_size = 50
enemy_x, enemy_y = random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size)
enemy_speed = 5

# Score tracking
score = 0
font = pygame.font.Font(None, 36)

# Recognizer setup
recognizer = sr.Recognizer()

def recognize_speech():
    global character_x, character_y
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for commands (say 'left', 'right', 'up', 'down')...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print("Recognized:", command)
            
            if "left" in command:
                character_x -= character_speed
            elif "right" in command:
                character_x += character_speed
            elif "up" in command:
                character_y -= character_speed
            elif "down" in command:
                character_y += character_speed
        except sr.UnknownValueError:
            print("Could not understand the command.")
        except sr.RequestError:
            print("Speech recognition service unavailable.")
        except Exception as e:
            print("Error:", str(e))

# Enemy movement
def move_enemy():
    global enemy_x, enemy_y
    if enemy_x < character_x:
        enemy_x += enemy_speed
    elif enemy_x > character_x:
        enemy_x -= enemy_speed
    if enemy_y < character_y:
        enemy_y += enemy_speed
    elif enemy_y > character_y:
        enemy_y -= enemy_speed

# Check collision
def check_collision():
    global score, enemy_x, enemy_y
    if abs(character_x - enemy_x) < character_size and abs(character_y - enemy_y) < character_size:
        score += 1
        print("Score:", score)
        enemy_x, enemy_y = random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (character_x, character_y, character_size, character_size))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    move_enemy()
    check_collision()
    
    # Start speech recognition in a separate thread to avoid freezing
    threading.Thread(target=recognize_speech, daemon=True).start()

pygame.quit()
