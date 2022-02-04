import sys
import pygame
from setings import Setings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from aliens import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()  # инициализация игры и создание экрана
    ai_setings = Setings()  # создание переменной дла сохранения класса с настройками в нее
    screen = pygame.display.set_mode(
        (ai_setings.screen_width, ai_setings.screen_heigth))  # передал размеры окна в переменную из файла setings
    pygame.display.set_caption('Alien invasion')  # создание названия которое отображается в шапке окна
    play_button = Button(ai_setings, screen, 'Play')
    stats = GameStats(ai_setings)
    sb=Scoreboard(ai_setings,screen,stats)
    ship = Ship(ai_setings, screen)
    bullets = Group()
    alien = Alien(ai_setings, screen)
    aliens = Group()
    gf.create_fleet(ai_setings, screen, ship, aliens)

    # запуск основного цикла игры
    while True:
        # отслеживание событий клавиатуры и мыши
        gf.chek_events(ai_setings, screen, stats,sb, play_button, ship, aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setings, screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ai_setings,screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_setings, screen, stats,sb, ship, aliens, bullets, play_button)


run_game()
