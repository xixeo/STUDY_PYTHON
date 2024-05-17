import pygame

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))

ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')

ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom
# ship_rect = pygame.rect.Rect(0,0,100,100)
alien_rect = pygame.rect.Rect(200,200,200,200)

bullet_rect = None
bullets = []

clock = pygame.time.Clock()

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 총알 땅땅
                # bullets = True
                bullet_rect = pygame.rect.Rect(0, 0, 5, 50)
                bullet_rect.midbottom = ship_rect.midtop
                bullets.append(bullet_rect)

            elif event.key == pygame.K_RIGHT:
                right_pressed = True
                # ship_rect.x = ship_rect.x + 10
                # alien_rect.x = alien_rect.x + 20
            elif event.key == pygame.K_LEFT:
                 left_pressed = True
                # ship_rect.x = ship_rect.x - 10
                # alien_rect.x = alien_rect.x - 20
            elif event.key == pygame.K_UP:
                 up_pressed = True
                # ship_rect.y = ship_rect.y - 10
                # alien_rect.y = alien_rect.y - 20
            elif event.key == pygame.K_DOWN:
                 down_pressed = True
                # ship_rect.y = ship_rect.y + 10
                # alien_rect.y = alien_rect.y + 20

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False

    # Do logical updates here.
    # ...
    if right_pressed: 
        ship_rect.x = ship_rect.x + 10
        alien_rect.x = alien_rect.x + 20

    if left_pressed: 
        ship_rect.x = ship_rect.x - 10
        alien_rect.x = alien_rect.x - 20
   
    if up_pressed: 
        ship_rect.y = ship_rect.y - 10
        alien_rect.y = alien_rect.y - 20

    if down_pressed: 
        ship_rect.y = ship_rect.y + 10
        alien_rect.y = alien_rect.y + 20

    if bullets:
        for bullet in bullets:
            bullet.y = bullet.y - 50
    
    screen_surf.fill((0, 0, 0))  # Fill the display with a solid color


    # Render the graphics here.
    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)
    if bullets:
           for bullet in bullets:
               pygame.draw.rect(screen_surf, 'yellow', bullet)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)