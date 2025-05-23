import sys
import pygame

def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)  

def check_keydown_events(event, ship):
        """"Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                ship.moving_left = True
              
def check_keyup_events(event, ship):
            """Реагирует на отпускание клавиш"""        
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                ship.rect.cenerx += 1