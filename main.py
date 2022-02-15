from sys import exit
import pygame

# Starts pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_surf = font.render('My game!', False, 'Black')
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    pygame.draw.rect(screen, 'Pink', score_rect, 6)
    screen.blit(score_surf, score_rect)

    snail_rect.x -= 2
    if snail_rect.x <= -100:
        snail_rect.x = 900

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect):
        # print("collision")

    # Draw all elements
    # and update everything
    pygame.display.update()
    clock.tick(60)
