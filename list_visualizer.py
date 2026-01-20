import random
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock() 
#"numbers" is a list, put in None matching list if you dont want to use that "feature"
class numbers_displayer:
  def __init__(self, WIDTH, HEIGHT, numbers, scale, line_width, window_name, matching_list):
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.numbers = numbers
    self.scale = scale
    self.line_width = line_width
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.numbers_length = len(numbers)
    self.matching_list = matching_list
    pygame.display.set_caption(window_name)

  def update_screen(self):
     place_increment = self.WIDTH / self.numbers_length
     place = place_increment / 2
     self.screen.fill(WHITE)    
     for i in range(self.numbers_length):
         if not self.matching_list:
             color = BLACK
         else:
             color = GREEN if self.matching_list[i] == self.numbers[i] else RED
         pygame.draw.line(
             self.screen, 
             color, 
             (place, self.HEIGHT - self.numbers[i] * self.scale), 
             (place, self.HEIGHT), 
             self.line_width
         )
         place += place_increment
     pygame.display.flip()


#example usage:
display= numbers_displayer(1000, 1000, [1, 2, 3], 1, 5, "example", [1, 2, 3])
screen.update_screen()

while True:
  clock.tick(67)
