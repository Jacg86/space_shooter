import pygame
import random
from utils import *
from player import Player
from enemy import Enemy
from bullet import Bullet

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()

    MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    state = MENU

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    player = Player()
    all_sprites.add(player)

    current_level = 1
    max_level = 10
    score = 0
    
    enemy_speed = 1
    enemy_drop_speed = 10

    def spawn_enemies(level):
        mobs.empty()
        bullets.empty()
        all_sprites.empty()
        all_sprites.add(player)
        
        rows = 3 + (level // 2)
        cols = 8
        
        if level >= 5:
            cols = 6
            
        if rows > 6: rows = 6
        
        for row in range(rows):
            for col in range(cols):
                x = 100 + col * 70
                y = 40 + row * 60
                m = Enemy(x, y, level)
                all_sprites.add(m)
                mobs.add(m)
    running = True
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if state == MENU:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        state = PLAYING
                        current_level = 1
                        score = 0
                        enemy_speed = 2
                        enemy_drop_speed = 10
                        spawn_enemies(current_level)       
            elif state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = player.shoot()
                        all_sprites.add(bullet)
                        bullets.add(bullet)          
            elif state == GAME_OVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        state = MENU

        if state == PLAYING:
            all_sprites.update()
            
            move_down = False
            for m in mobs:
                m.speed_x = enemy_speed
                if m.rect.right >= SCREEN_WIDTH or m.rect.left <= 0:
                    move_down = True
            
            if move_down:
                enemy_speed *= -1
                for m in mobs:
                    m.rect.y += enemy_drop_speed
                    m.speed_x = enemy_speed
            hits = pygame.sprite.groupcollide(mobs, bullets, False, True)
            for mob, hit_bullets in hits.items():
                for b in hit_bullets:
                    mob.hp -= 1
                    if mob.hp <= 0:
                        mob.kill()
                        score += 10 * mob.level 
                        if mob.is_big:
                            score += 50
            hits = pygame.sprite.spritecollide(player, mobs, False)
            if hits:
                state = GAME_OVER
            for m in mobs:
                if m.rect.bottom >= SCREEN_HEIGHT:
                    state = GAME_OVER
            for m in mobs:
                if m.rect.bottom >= SCREEN_HEIGHT:
                    state = GAME_OVER
            if len(mobs) == 0:
                current_level += 1
                if current_level > max_level:
                    current_level = max_level 
                    enemy_speed = 10 
                else:
                    enemy_speed = abs(enemy_speed) + 1 
                    if enemy_speed > 10: enemy_speed = 10
                    enemy_drop_speed += 2            
                spawn_enemies(current_level)
                enemy_speed = abs(enemy_speed) 

        screen.fill(BLACK)
        
        if state == MENU:
            draw_text(screen, "SPACE INVADERS", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
            draw_text(screen, "Usa las flechas para moverte", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            draw_text(screen, "Espacio para disparar", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30)
            draw_text(screen, "Presiona ENTER para jugar", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
            
        elif state == PLAYING:
            all_sprites.draw(screen)
            draw_text(screen, f"Score: {score}", 18, SCREEN_WIDTH / 2, 10)
            draw_text(screen, f"Level: {current_level}", 18, SCREEN_WIDTH - 50, 10)
            
        elif state == GAME_OVER:
            draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
            draw_text(screen, "Puntaje: " + str(score), 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            draw_text(screen, "Presiona ENTER para volver al menú", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
