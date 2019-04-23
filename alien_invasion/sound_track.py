import pygame
pygame.mixer.init()
def sound_track1():
	track = pygame.mixer.music.load('Lorne Balfe - Fight Club.mp3')
	pygame.mixer.music.play(loops = -1)

def sound_track2():
	track = pygame.mixer.music.load('Andreas Waldetoft - Operation barbarossa.mp3')
	pygame.mixer.music.play(loops = -1)

def sound_track3():
	track = pygame.mixer.music.load('Inon Zur - Fallout 4 Main Theme.mp3')
	pygame.mixer.music.play(loops = -1)
	
def sound_track4():
	track = pygame.mixer.music.load('Ben Prunty-MilkyWay.mp3')
	pygame.mixer.music.play(loops = -1)	
