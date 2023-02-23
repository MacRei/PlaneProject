import pygame, os, sys, random

pygame.init()
clock = pygame.time.Clock()
currentTime = 0

screen = pygame.display.set_mode((1120, 630)) #16:9 * 60
pygame.display.set_caption("Roaring Skies? Speeding Skies?")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\BiPlane.png")), (176.4, 84))
        self.rect = pygame.Rect(0, 0, 140, 44) #126, 60 * 1.3
    def update(self):
        global playerYPos, playerXPos
        self.rect.x = playerXPos
        self.rect.y = playerYPos
        if self.rect.x > 300:
            playerXPos = 299
        if self.rect.x < 0:
            playerXPos = 1
        if self.rect.y > 575:
            playerYPos = 574
        if self.rect.y < 10:
            playerYPos = 9
        #pygame.draw.rect(screen, (255, 0, 0), self.rect)
        self.rect = pygame.Rect.move(self.rect, -20, -20)
player = Player()
playerGroup = pygame.sprite.Group()
playerGroup.add(player)
playerYPos = 100
playerXPos = 100
playerSpeed = 2
playerYChange = 0
playerXChange = 0
health = 3
alive = True

class Cloud(pygame.sprite.Sprite):
    def __init__(self, which, posX, posY):
        super().__init__()
        if which == 1: #205, 85
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds1.png")), (266.5, 110.5))
        if which == 2:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds2.png")), (266.5, 110.5))
        if which == 3: 
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds3.png")), (266.5, 110.5))
        if which == 4: 
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds4.png")), (266.5, 110.5))
        if which == 5:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds5.png")), (266.5, 110.5))
        if which == 6: 
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds6.png")), (266.5, 110.5))
        if which == 7: 
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds7.png")), (266.5, 110.5))
        if which == 8:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds8.png")), (266.5, 110.5))
        if which == 9: 
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds9.png")), (266.5, 110.5))
        if which == 10: 
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Clouds\Clouds10.png")), (266.5, 110.5))
        self.rect = pygame.Rect(posX, posY, 266.5, 110.5)
    def update(self):
        self.rect.x -= 1 * parallaxSpeed
        if self.rect.x < -250:
            cloud = Cloud(random.randint(1, 10), 1120, random.randint(-40, 200))
            cloudGroup.add(cloud)
            self.kill()
cloudGroup = pygame.sprite.Group()
for cloudRepeat in range(9):
    cloud = Cloud(random.randint(1, 10), (cloudRepeat * 300), random.randint(-40, 200))
    cloudGroup.add(cloud)
parallaxSpeed = 1

class Missile(pygame.sprite.Sprite):
    def __init__(self, posY, which):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Missiles\Missiles1.png")), (109.2, 15.6))
        self.rect = pygame.Rect(-300, posY, 100, 13)
        self.whichMissile = which
        self.animationTimer = pygame.time.get_ticks()
        self.touching = False
    def update(self):
        global health
        self.rect.x += 2
        if self.rect.x > 1200:
            self.kill()
        if self.rect.colliderect(player.rect) and self.touching == False:
            health -= 1
            self.touching = True
        if self.rect.colliderect(player.rect) == False:
            self.touching = False
        if self.whichMissile == "Regular":
            if currentTime - self.animationTimer < 200:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Missiles\Missiles1.png")), (109.2, 15.6))
            elif currentTime - self.animationTimer < 400:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Missiles\Missiles2.png")), (109.2, 15.6))
            elif currentTime - self.animationTimer < 800:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\reill\OneDrive\Documents\Code\PlaneProjectAssets\PlaneProjectArt\Missiles\Missiles3.png")), (109.2, 15.6))
            elif currentTime - self.animationTimer < 1200:
                self.animationTimer = pygame.time.get_ticks()
missileGroup = pygame.sprite.Group()
missileRespawnCheck = 0
def MissileSpawnerManager():
    global missileRespawnCheck
    if currentTime - missileRespawnCheck > 1000:
        missile = Missile(random.randint(0, 600), "Regular")
        missileGroup.add(missile)
        missileRespawnCheck = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerYChange += (-1 * playerSpeed)
            if event.key == pygame.K_s:
                playerYChange += (1 * playerSpeed)
            if event.key == pygame.K_a:
                playerXChange += (-1 * playerSpeed)
            if event.key == pygame.K_d:
                playerXChange += (1 * playerSpeed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerYChange += (1 * playerSpeed)
            if event.key == pygame.K_s:
                playerYChange += (-1 * playerSpeed)
            if event.key == pygame.K_a:
                playerXChange += (1 * playerSpeed)
            if event.key == pygame.K_d:
                playerXChange += (-1 * playerSpeed)
      
    playerXPos += playerXChange
    playerYPos += playerYChange

    MissileSpawnerManager()

    if health < 1:
        alive = False

    screen.fill((66, 130, 179))
    cloudGroup.draw(screen)
    missileGroup.draw(screen)
    if alive == True:
        playerGroup.draw(screen)

    cloudGroup.update()
    missileGroup.update()
    playerGroup.update()

    pygame.display.flip()
    currentTime = pygame.time.get_ticks()
    clock.tick(60)