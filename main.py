# -*- coding: utf-8 -*-
"""
Created on January 8 2019

@author: Alexi
"""

import pygame
from enum import Enum

def pprint(message):
  print message

class MenuState(Enum):
  opening_menu = 0
  player_count_menu = 1
  in_game = 2

class App: #a game client
  def __init__(self):
    self.play_on = True #false means quit the client
    self.screen_width = 800
    self.screen_height = 800
    self.menu_state = MenuState.opening_menu
    pygame.init()
    self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
    self.title_font = pygame.font.SysFont('Average', 60)
    self.menu_font = pygame.font.SysFont('Average', 30)
    self.clickables = []
    self.redraw = True #Flag for redrawing the screen

  def open_player_count_menu(self):
    self.redraw = True
    self.menu_state = MenuState.player_count_menu
    self.player_count = 2
    self.game_mode = "hotseat"

  def open_opening_menu(self):
    self.redraw = True
    self.menu_state = MenuState.opening_menu

  def launch_game(self):
    print "WE HAVE LIFTOFF!"
    self.redraw = True
    self.menu_state = MenuState.in_game
    #TODO

  def highlight2(self): #player count 2
    self.redraw = True
    self.player_count = 2

  def highlight3(self): #player count 3
    self.redraw = True
    self.player_count = 3

  def highlight4(self): #player count 4
    self.redraw = True
    self.player_count = 4

  def on_execute(self): #start a new game client instance
    #NOTE initialize first, THEN call on_execute
    while self.play_on:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.play_on = False
        elif event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          [clicked_on[0]() for clicked_on in self.clickables if clicked_on[1].collidepoint(pos)]
        else:
          pass #TODO do something with events
      self.update() #draw updates
    pygame.quit()

  def update(self):
    if not self.redraw:
      return #Nothing's changed. Just return.
    if self.menu_state == MenuState.opening_menu:
      self.clickables = [] #Reset the clickables
      self.draw_opening_menu()
    elif self.menu_state == MenuState.player_count_menu:
      self.clickables = [] #Reset the clickables
      self.draw_player_count_menu()
    elif self.menu_state == MenuState.in_game:
      self.clickables = [] #Reset the clickables
      self.draw_game()
    else:
      pass #TODO
    pygame.display.flip() #pygame is double-buffered. this swaps for viz.
    self.redraw = False

  def draw_background(self):
    self.screen.fill((0,0,0))

  def draw_opening_menu(self):
    self.draw_background()
    message = "Welcome to WARP GATE."
    self.draw_boxed_text(message,(100,100),False,True)
    self.draw_boxed_text("Play a hotseat game.",(100,300),self.open_player_count_menu)

  def draw_player_count_menu(self):
    self.draw_background()
    self.draw_boxed_text("How many players for",(100,100),False,True)
    self.draw_boxed_text("HOTSEAT game?",(100,180),False,True)
    pygame.draw.rect(self.screen, (60,20,20), #TODO fix colors
        pygame.Rect((self.player_count-1)*100-30,270,71,81))#textw 11 / texth 21 / box 20 / border 10
    self.draw_boxed_text("2",(100,300),self.highlight2)
    self.draw_boxed_text("3",(200,300),self.highlight3)
    self.draw_boxed_text("4",(300,300),self.highlight4)
    self.draw_boxed_text("Begin Game",(100,500),self.launch_game)
    self.draw_boxed_text("Back",(700,700),self.open_opening_menu)

  def draw_game(self):
    self.draw_background()
    self.draw_boxed_text("LOTS TODO",(300,300),False,True)

  def draw_boxed_text(self,message,position,clickable=False,title=False):
    if title:
      text_surface = self.title_font.render(message, False, (255,255,255))
      text_width, text_height = self.title_font.size(message)
    else:
      text_surface = self.menu_font.render(message, False, (255,255,255))
      text_width, text_height = self.menu_font.size(message)
      #print "Text:",message,"Width/Height:",text_width,text_height
    rect_object = pygame.draw.rect(self.screen, (30,30,30),
        pygame.Rect(position[0]-20,position[1]-20,text_width+40,text_height+40))
    self.screen.blit(text_surface,position)
    if clickable != False:
      self.clickables.append((clickable,rect_object)) #(method to call if clicked, clickable space)

if __name__=="__main__":
  theApp = App()
  theApp.on_execute()
