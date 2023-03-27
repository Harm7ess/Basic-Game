import pygame

pygame.init()

altura = 400
largura = 400

x = 400/2
y = 400/2

tela = pygame.display.set_mode((altura, largura))

pygame.display.set_caption("Basic Game")
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.guit()
               exit()

          pygame.draw.circle(tela, (255, 0, 0), (x, y), 40)

          
    
    pygame.display.update()
