import pygame
 
pygame.init()
pantalla = pygame.display.set_mode((600, 400))
reloj = pygame.time.Clock()
h = False
 
font = pygame.font.SysFont("comicsansms", 50)
 
text = font.render("Hola Mundo :) ", True, (0, 128, 0))
 
while not h:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            h = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            h = True
 
    pantalla.fill((25))
    pantalla.blit(text,(300 - text.get_width() // 2, 200 - text.get_height() // 2))
 
    pygame.display.flip()
    reloj.tick(60)
