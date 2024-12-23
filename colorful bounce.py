import pygame 
import random
pygame.init()
SPRITE_COLORCHANGE=pygame.USEREVENT+1
BACKGROUND_COLORCHANGE=pygame.USEREVENT+2
Blue=pygame.color("blue")
Lightblue=pygame.color("lightblue")
Darkblue=pygame.color("darkblue")
Yellow=pygame.color("yellow")
Indigo=pygame.color("indigo")
Orange=pygame.color("orange")
White=pygame.color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
         self.velocity[1] = -self.velocity[1]
         boundary_hit = True
    if boundary_hit:
      pygame.event.post(pygame.event.Event(SPRITE_COLORCHANGE))
      pygame.event.post(pygame.event.Event(BACKGROUND_COLORCHANGE))
    def change_background_color():
     global bg_color
     bg_color = random.choice([Blue,Lightblue,Darkblue])
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(White, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)
screen=pygame.display.set_mode(500,400)
screen.fill("blue")
exit=False
while not exit:
   if pygame.event.get()==QUIT:
      quit()