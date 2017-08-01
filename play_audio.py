import pygame
file = 'name.mp3'#file name
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
clock=pygame.time.Clock()
pygame.mixer.music.play()
while True:
	clock.tick()
pass
