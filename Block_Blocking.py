import pygame
from random import randrange
from pygame.locals import *
from sys import exit

pygame.init()

largura = 540
altura = 960
contagem = 0

cinza = pygame.Color(226, 226, 226)
font = pygame.font.SysFont('fixtureexpandedmedium', 200)
click = False

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
acertos = font.render(str(contagem), True, (175, 175, 175))


def menu():
    while True:        
        butao = pygame.Rect(190, 688, 150, 75)
        tela.blit(bg, (0, 0))
        tela.blit(marca, (75, 300))
        # tela.blit(play, (250, 700))
        mx, my = pygame.mouse.get_pos()
        if butao.collidepoint((mx, my)):
            if click:
                game()
        pygame.draw.rect(tela, (175, 175, 175), butao)
        tela.blit(play, (245, 700))
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        if event.type == KEYDOWN:
            pygame.quit()
            exit()
            
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
                 
        
        
        pygame.display.flip()


def game():
    rot_ret = 0
    pos_x = 50
    pos_y = -25
    ret_preto = pygame.transform.rotate(pygame.image.load('imagens/ret_preto.png'), rot_ret)
    
    # ret_preto = pygame.Rect(pos_x, pos_y, 50, 50)
    
    pos_play = 250
    running = True
    while running:
        tela.blit(bg, (0, 0))
        tela.blit(suporte, (20, 480))
        tela.blit(jogador, (pos_play, 480))        
        tela.blit(acertos, (185, 600))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
        if pygame.key.get_pressed()[K_LEFT]:
            pos_play = pos_play - 5
            if pos_play <= 20:
                pos_play = 20                      

        if pygame.key.get_pressed()[K_RIGHT]:
            pos_play = pos_play + 5
            if pos_play >= 450:
                pos_play = 450  

        
        tela.blit(ret_preto, (pos_x, pos_y))
        if pos_y >= altura:
            pos_y = -25
            pos_x = randrange(40, 500, 100)
        pos_y = pos_y + 3
        rot_ret = rot_ret + 3
        
        
                       
        
        pygame.display.flip()

menu()