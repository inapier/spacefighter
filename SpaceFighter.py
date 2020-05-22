import pygame, random, sys
import pickle

W = 848  # window width
H = 848  # window height
FPS = 60 # frames per second

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



all_sprites = pygame.sprite.Group() #instance of sprite container
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
pygame.init()

bg = player_img = enemy1_img = enemy2_img = bullet_img = screen = player = enemy = clock = font = bg_rect = None
ENEMIES = []
hsFile = ''
savedHS = 0

def play_again ():
    replay = False

    replay_text = font.render("Press 'R' to play again! Or any key to exit.", True, WHITE)
    screen.blit(replay_text, (200, 400))
    pygame.display.flip()

    while not pygame.event.peek(pygame.KEYDOWN):
        pass

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                replay = True

    return replay
            


class Player(pygame.sprite.Sprite):  #defining player class
    def __init__(self, player_img, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.bullet_img = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 424
        self.rect.bottom = 838
        self.speedx = 0
        self.count = 0
        self.score = 0
        self.health = 4

    def update(self): #checks for input
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]: #negative value on X axis
            self.speedx = -8
        if keystate[pygame.K_RIGHT]: #positive on X
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > W: #checks if player position is greater than the width of the window. Prevents player from moving off screen.
            self.rect.right = W
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self): #shooting the bullet.
        self.count += 1
        if self.count > 5:
            self.count = 0


        bullet = Bullet(self.rect.centerx, self.rect.top, self.bullet_img)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite): # Defining bullet behavior
    def __init__ (self, x, y, bullet_img):
         pygame.sprite.Sprite.__init__(self)
         self.image = bullet_img
         self.rect = self.image.get_rect()
         self.rect.bottom = y
         self.rect.centerx = x
         self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()  #destroys bullet instance once it's off screen


class Enemy(pygame.sprite.Sprite): #defining enemy class
    def __init__(self, ENEMIES):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(ENEMIES)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = 7

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > H + 10:
            self.rect.x = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        if self.rect.bottom > 848:
            self.kill()

def init():
    global bg, screen, player, enemy, clock, ENEMIES, font, hsFile, savedHS, bg_rect

    bg_rect = bg.get_rect()

    ENEMIES = [enemy1_img, enemy2_img]

    # pygame.init()
    hsFile = "Highscore.pkl"  #load the pickle file
    try:
        f = open(hsFile, 'rb')
        savedHS = pickle.load(f)
        print(savedHS)
    except OSError:
        savedHS = 0

    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Space Fighter")
    font = pygame.font.SysFont('couriernew', 16)

    clock = pygame.time.Clock()

    player = Player(player_img, bullet_img)
    enemy = Enemy(ENEMIES)
    all_sprites.add(player)
    all_sprites.add(enemy)
    enemies.add(enemy)

def main_loop():
    running = True

    while running:
        clock.tick(FPS)

        if len(enemies.sprites()) > 0: #if there are enemies on screen, check for collision and add to score
            contact = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for collision in contact:
                enemy = Enemy(ENEMIES)
                all_sprites.add(enemy)
                enemies.add(enemy)
                player.score += 1
                print(player.score)
            contact = pygame.sprite.spritecollide(player, enemies, False)
            if contact:
                for con in contact:
                    con.kill()
                
                player.health -= 1
                if player.health <= 0:
                    running = False

        else: #if no enemies on screen, instantiate an enemy and add it to the sprites group
            enemy = Enemy(ENEMIES)
            all_sprites.add(enemy)
            enemies.add(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        all_sprites.update()

        highScore = font.render("Highscore: " + str(savedHS), True, WHITE)
        score = font.render("Current Score: " + str(player.score), True, WHITE)
        health = font.render("Current Lives: " + str(player.health), True, WHITE)

        screen.blit(bg, bg_rect)
        screen.blit(highScore, (550, 10)) #draw highScore object
        screen.blit(score, (550, 30)) #draw score object
        screen.blit(health, (550, 60))
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill(BLACK)

def cleanup():
    if player.score > savedHS: #if the player score is greater than the value of 'savedHS' overwrite and save the new score.
        f = open(hsFile, 'wb') #save player.score to hsFile
        pickle.dump(player.score, f)
        f.close()

    all_sprites.remove(player)

def main():
    global bg, player_img, bullet_img, enemy1_img, enemy2_img

    # load images
    bg = pygame.image.load("space.png") #background image
    player_img = pygame.image.load('ship.png') #player image
    bullet_img = pygame.image.load("bullet.png") #bullet image
    enemy1_img = pygame.image.load("enemy1.png") #enemy1 image
    enemy2_img = pygame.image.load("enemy2.png") #enemy2 image


    replay = True
    while replay:
        init()
        main_loop()
        cleanup()
        replay = play_again()

    pygame.quit() 

if __name__ == "__main__":
    main()