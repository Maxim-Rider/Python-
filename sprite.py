import pygame
import random
 
pygame.init()
 
CARS = ['car1.png', 'car2.png', 'car3.png']
 
 
pygame.time.set_timer(pygame.USEREVENT, 200)
FPS = 60
SCREEN = (600, 400)
BLACK = (0, 0, 0)
GAME_OVER = False
sc = pygame.display.set_mode(SCREEN)
 
 
pygame.mixer.music.load('car.mp3')
pygame.mixer.music.play(-1)
boom = pygame.mixer.Sound("boom.wav")
 
game_over_text = pygame.font.SysFont('arial', 36).render("GAME OVER", 1, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(SCREEN[0]//2, SCREEN[1]//2))
 
 
class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = random.randint(2, 7)
        self.add(group)
 
    def update(self, *args):
        if self.rect.y < SCREEN[1]:
            self.rect.y += self.speed
        else:
            self.kill()
 
 
class HeroCar(pygame.sprite.Sprite):
    def __init__(self, X, path, group):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(X, SCREEN[1]))
        self.add(group)
 
    def update(self, move):
        if move == "LEFT":
            self.rect.x -= 3
        elif move == "RIGHT":
            self.rect.x += 3
 
 
hero_group = pygame.sprite.Group()
hero = HeroCar(SCREEN[0]//2, 'car.png', hero_group)
 
 
cars = pygame.sprite.Group()
play = True
 
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
 
        if event.type == pygame.USEREVENT and not GAME_OVER:
            surf = pygame.image.load(CARS[random.randint(0, 2)]).convert_alpha()
            x = random.randint(1, SCREEN[0])
            Car(x, surf, cars)
 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            pygame.mixer.music.play(-1)
            GAME_OVER = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < SCREEN[0] and not GAME_OVER:
        hero_group.update('RIGHT')
 
    if keys[pygame.K_LEFT] and hero.rect.x > 0 and not GAME_OVER:
        hero_group.update('LEFT')
 
    sc.fill(BLACK)
 
    hero_group.draw(sc)
 
    cars.draw(sc)
    cars.update()
 
    if pygame.sprite.spritecollideany(hero, cars):
        GAME_OVER = True
        cars.empty()
        hero.rect.x = SCREEN[0]//2
        pygame.mixer.music.stop()
        boom.play()
 
    if GAME_OVER:
        sc.blit(game_over_text, game_over_rect)
 
    pygame.display.update()
 
    pygame.time.Clock().tick(FPS)