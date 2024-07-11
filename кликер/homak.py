import pygame, sys
pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

homak = pygame.Rect(WIDTH/2-250,HEIGHT/2-150,500,400)
homak_img = pygame.image.load('Sprite2-0001.png')
homak_img = pygame.transform.scale(homak_img, (homak.width, homak.height))

score=0
font = pygame.font.SysFont('Arial', 100)
score_text = font.render(str(score), False, (255, 0, 0))
click = 1
while True:
    screen.fill((255,255,255))
    screen.blit(homak_img,homak)
    screen.blit(score_text, (WIDTH/2-50,HEIGHT/2-350))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:

            sys.exit("froget")
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if homak.collidepoint(e.pos[0], e.pos[1]):
                score += click
                score_text = font.render(str(score), False, (255, 0, 0))

    pygame.display.update()
    clock.tick(60)