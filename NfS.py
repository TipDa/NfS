from pygame import *
win_width = 800
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('NfS')
back = transform.scale(image.load('kartina.jpg'), (win_width, win_height))

class bord(sprite.Sprite):
    def __init__(self, color1, color2, color3, x, y, width, height):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_bord(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, width, height, speed):
        self.image = transform.scale(image.load(p_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_player(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_enemy(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


font.init()
font1 = font.SysFont('Arial', 70)
lose = font1.render('Ты проиграл', True, (180,0,0))
lose1 = font1.render('Ты наехал на говно!!', True, (180,0,0))
lose2 = font1.render('Мусор в говне!!', True, (180,0,0))
win = font1.render('Ты выйграл', True, (180,0,0))



goal = GameSprite('download.png', 50,150, 100,100, 0)
player = Player('image.jpg',110,550, 40,40, 5)
enemy = Player('images.jpg',110,650, 40,40, 5)
pomeha = Player('download.jpg',500,210, 40,40, 5)
pomeha1 = Player('download.jpg',650,350, 40,40, 5)
pomeha2 = Player('download.jpg',500,610, 40,40, 5)


b1 = bord(128,0,0, 100,400, 5,250)
b2 = bord(128,0,0, 200,500, 5,150)
b3 = bord(128,0,0, 300,400, 5,150)
b4 = bord(128,0,0, 100,400, 200,5)
b5 = bord(128,0,0, 200,650, 550,5)
b6 = bord(128,0,0, 300,550, 350,5)
b7 = bord(128,0,0, 750,150, 5,500)
b8 = bord(128,0,0, 650,250, 5,300)
b9 = bord(128,0,0, 50,150, 700,5)
b10 = bord(128,0,0, 50,250, 600,5)


finish = False
game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(back, (0, 0))
        b1.draw_bord()
        b2.draw_bord()
        b3.draw_bord()
        b4.draw_bord()
        b5.draw_bord()
        b6.draw_bord()
        b7.draw_bord()
        b8.draw_bord()
        b9.draw_bord()
        b10.draw_bord()
        goal.reset()
        player.update_player()
        enemy.update_enemy()
        pomeha.update()
        pomeha1.update()
        pomeha2.update()
        pomeha.reset()
        pomeha1.reset()
        pomeha2.reset()
        player.reset()
        enemy.reset()
        if sprite.collide_rect(player, goal):
            finish = True
            window.blit(win, (200,200))
        if sprite.collide_rect(enemy, goal):
            finish = True
            window.blit(lose, (200,200))
        if sprite.collide_rect(player, b1) or sprite.collide_rect(player, b2) or sprite.collide_rect(player, b3) or sprite.collide_rect(player, b4) or sprite.collide_rect(player, b5) or sprite.collide_rect(player, b6) or sprite.collide_rect(player, b7) or sprite.collide_rect(player, b8) or sprite.collide_rect(player, b9) or sprite.collide_rect(player, b10):
            finish = True
            window.blit(lose, (200,200))
        if sprite.collide_rect(enemy, b1) or sprite.collide_rect(enemy, b2) or sprite.collide_rect(enemy, b3) or sprite.collide_rect(enemy, b4) or sprite.collide_rect(enemy, b5) or sprite.collide_rect(enemy, b6) or sprite.collide_rect(enemy, b7) or sprite.collide_rect(enemy, b8) or sprite.collide_rect(enemy, b9) or sprite.collide_rect(enemy, b10):
            finish = True
            window.blit(win, (200,200))
        if sprite.collide_rect(player, enemy):
            finish = True
            window.blit(lose, (200,200))
        if sprite.collide_rect(pomeha, player):
            window.blit(lose1, (100,100))
        if sprite.collide_rect(pomeha1, player):
            window.blit(lose1, (100,100))
        if sprite.collide_rect(pomeha2, player):
            window.blit(lose1, (100,100))
        if sprite.collide_rect(pomeha, enemy):
            window.blit(lose2, (100,100))
        if sprite.collide_rect(pomeha1, enemy):
            window.blit(lose2, (100,100))
        if sprite.collide_rect(pomeha2, enemy):
            window.blit(lose2, (100,100))
    display.update()
    clock.tick(60)