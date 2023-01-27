import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 540
altura = 960
pos_play = 250
contagem = 0
cinza = pygame.Color(226, 226, 226)
font = pygame.font.SysFont('fixtureexpandedmedium', 200)

# print(pygame.font.get_fonts())


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Block Blocking')

# jogador = pygame.transform.scale(pygame.image.load('imagens/jogador.png'), (100, 18))
jogador = pygame.image.load('imagens/jogador.png')
marca = pygame.image.load('imagens/marca.png')
play = pygame.image.load('imagens/play.png')
retorno = pygame.image.load('imagens/return.png')
suporte = pygame.image.load('imagens/suporte.png')
bg = pygame.image.load('imagens/bg.png')
acertos = font.render('2', True, (175, 175, 175))
# bg = pygame.draw.rect(tela, cinza, (0, 0, 540, 960))




while True:
    tela.blit(bg, (0, 0))
    tela.blit(suporte, (20, 480))
    tela.blit(jogador, (pos_play, 480))
    tela.blit(acertos, (200, 600))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_LEFT:
        #         pos_play = pos_play - 10  
                                         
        #     if event.key == K_RIGHT:
        #         pos_play = pos_play + 10
    
    if pygame.key.get_pressed()[K_LEFT]:
        pos_play = pos_play - 5
    if pygame.key.get_pressed()[K_RIGHT]:
        pos_play = pos_play + 5
                
    

    


    pygame.display.update()