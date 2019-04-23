#!/usr/bin/env python
#coding=utf-8
import sys

import pygame
from sound_track import *
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from aerolite import Aerolite
import game_functions as gf
from pygame.sprite import Group


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN, 32)
	pygame.display.set_caption("Alien Invasion")
	pygame.display.set_icon(pygame.image.load('images/alien.bmp'))
	bg_image = pygame.image.load("space.jpg")
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	ship = Ship(ai_settings, screen)
	sb = Scoreboard(ai_settings, screen, stats)
	aerolite = Aerolite(ai_settings, screen)
	
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings, screen, ship, aliens)
	sound_track3()
	
	while True:
		#screen.blit(bg_image, (0,0))
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, bg_image)
		
run_game()
		
