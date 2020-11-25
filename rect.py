import pygame
 
FPS = 5
W = 400
W2 = W//2
H = 400
H2 = H//2
WHITE = (255, 255, 255)
GREY = (170, 170, 170)
BLACK = (0, 0, 0)
 
rect1 = pygame.Rect((0,0,H2,W2))
rect2 = pygame.Rect((H2,0,H2,W2))
rect3 = pygame.Rect((0,W2,H2,W2))
rect4 = pygame.Rect((H2,W2,H2,W2))
 
pygame.init()
sc = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
key = 0
col_rand = 0
 
while True:
    sc.fill(WHITE)
 
    if col_rand == 0:
        color = GREY
        col_rand += 1
    else:
        color = BLACK
        col_rand = 0
 
    pygame.draw.circle(sc, color, (W2, H2), H2)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_1:
                key = 1
            elif i.key == pygame.K_2:
                key = 2
            elif i.key == pygame.K_0:
                key = 0
 
    if key == 0:
        pygame.display.update()
    elif key == 1:
        pygame.display.update([rect1, rect4])
    elif key == 2:
        pygame.display.update([rect2, rect3])
 
    clock.tick(FPS)