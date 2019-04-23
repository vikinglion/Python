#coding=utf-8
import pygame
from random import randrange
from pygame.sprite import Sprite
from pygame.locals import *

class Aerolite(Sprite):
	def __init__(self, ai_settings, screen):
		super(Aerolite, self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		
		
		#绘制Sprite对象时要用到的图像和矩形:
		self.image = pygame.image.load("aerolite.png")
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		

	def reset(self):
		#将陨石移到屏幕顶端的一个随机的位置
		self.rect.top = -self.rect.height
		self.rect.centerx = randrange(self.ai_settings.screen_width)
	
	def update(self):
		#更新下一帧的陨石
		self.rect.top += self.ai_settings.aerolite_speed
		
		if self.rect.top > self.ai_settings.screen_height:
			self.reset()
		
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	
