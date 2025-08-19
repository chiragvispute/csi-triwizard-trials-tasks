import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the theme song
pygame.mixer.music.load("Task-11(Pygame)/harry_potter_theme.mp3")

# Play the music
pygame.mixer.music.play()

# Keep the program running until the song ends
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

print("Enjoy the Harry Potter Theme Song! 🎵")
