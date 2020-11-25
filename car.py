import pygame
 
pygame.init()
 
FPS = 60
SCREEN = (600, 400)
WHITE = (255, 255, 255)

 
sc = pygame.display.set_mode(SCREEN)
sc.fill(WHITE)
car_surf_main = pygame.image.load('car.png').convert_alpha()
car_surf = car_surf_main
car_rect = car_surf_main.get_rect(center=(300, 200))
sc.blit(car_surf_main, car_rect)
pygame.display.update()
 
 
play = True
 
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            pygame.quit()
 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            car_surf = pygame.transform.rotate(car_surf_main, -90)
 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            car_surf = pygame.transform.rotate(car_surf_main, 90)
 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            car_surf = car_surf_main
 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            car_surf = pygame.transform.rotate(car_surf_main, 180)
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and car_rect.x + car_rect.height < SCREEN[0]:
        car_rect.x += 3
 
    if keys[pygame.K_LEFT] and car_rect.x > 0:
        car_rect.x -= 3
 
    if keys[pygame.K_UP] and car_rect.y > 0:
        car_rect.y -= 3
 
    if keys[pygame.K_DOWN] and car_rect.y + car_rect.height < SCREEN[1]:
        car_rect.y += 3
 
    sc.fill(WHITE)
    sc.blit(car_surf, car_rect)
    pygame.display.update()
 
    pygame.time.Clock().tick(FPS)