import sys
from time import sleep
import pygame
from bullet import Bullet
from aliens import Alien


def check_keydown_events(event, ai_setings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_setings, screen, ship, bullets):
    if len(bullets) < ai_setings.bullet_allowed:
        new_bullet = Bullet(ai_setings, screen, ship)
        bullets.add(new_bullet)


def chek_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def chek_events(ai_setings, screen,stats,sb,play_button, ship,aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_setings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)

def check_play_button(ai_setings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_cliked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_cliked and not stats.game_active:
        ai_setings.initialize_dynamic_setings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setings, screen, ship, aliens)
        ship.center_ship()





def update_screen(ai_setings, screen,stats,sb, ship, aliens, bullets,play_button):
    screen.fill(ai_setings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

    # При каждом проходе цикла перерисовывается экран.
    # отображение последнего отрисованного экрана


def update_bullets(ai_setings, screen,stats,sb, ship, aliens, bullets):
    bullets.update()
    for bulet in bullets.copy():
        if bulet.rect.bottom <= 0:
            bullets.remove(bulet)
    chek_bullet_alien_collisions(ai_setings, screen,stats,sb, ship, aliens, bullets)


def chek_bullet_alien_collisions(ai_setings, screen,stats,sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setings.alien_points*len(aliens)
        sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_setings.increase_speed()
        stats.level+=1
        sb.prep_level()
        create_fleet(ai_setings, screen, ship, aliens)


def get_number_aliens_x(ai_setings, alien_width):
    avilable_space_x = ai_setings.screen_width - 2 * alien_width
    number_aliens_x = int(avilable_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_setings, ship_heigth, alien_heigth):
    avilable_space_y = (ai_setings.screen_heigth - (3 * alien_heigth) - ship_heigth)
    number_rows = int(avilable_space_y / (2 * alien_heigth))
    return number_rows


def create_alien(ai_setings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_setings, screen, ship, aliens):
    alien = Alien(ai_setings, screen)

    number_aliens_x = get_number_aliens_x(ai_setings, alien.rect.width)
    number_rows = get_number_rows(ai_setings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_setings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setings, aliens)
            break


def change_fleet_direction(ai_setings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setings.fleet_drop_speed
    ai_setings.fleet_direction *= -1


def ship_hit(ai_setings,screen, stats,sb, ship, aliens, bullets):
    if stats.ship_left>0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)


def chek_aliens_bottom(ai_setings,screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setings,screen, stats, sb, ship, aliens, bullets)



def update_aliens(ai_setings,screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(ai_setings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setings,screen,stats,sb, ship, aliens, bullets)
    chek_aliens_bottom(ai_setings,screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()


