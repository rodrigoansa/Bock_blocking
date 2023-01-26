import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

largura = 600
altura = 520
pos_car_1 = -150
pos_car_2 = -250
pos_car_3 = -150
pos_car_4 = -450
pos_car_5 = -450
pos_tro_1 = -250
pos_tro_2 = -550
pos_tro_21 = -750
pos_tro_3 = -150
pos_tro_31 = -450
pos_ped = -250
pos_ped1 = -650
pos_sap_x = 280
pos_sap_y = 480
sapo_rot = 0

#Importando imagens
pista = pygame.image.load('imagens/road.png')
rio = pygame.image.load('imagens/rio.png')
car_1 = pygame.image.load('imagens/car_1.png')
car_1_rect = car_1.get_rect()
car_2 = pygame.image.load('imagens/car_2.png')
car_3 = pygame.image.load('imagens/car_3.png')
car_4 = pygame.image.load('imagens/car_4.png')
car_5 = pygame.image.load('imagens/car_5.png')
tronco_1 = pygame.image.load('imagens/tronco_1.png')
tronco_2 = pygame.image.load('imagens/tronco_2.png')
tronco_3 = pygame.image.load('imagens/tronco_3.png')
pedra = pygame.image.load('imagens/pedra.png')
sapo = pygame.image.load('imagens/sapo.png')
sapo_rect = sapo.get_rect()
# sapo_angulo = pygame.transform.rotate(sapo, sapo_rot)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jumper Frog')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                pos_sap_x = pos_sap_x - 70  
                pygame.transform.rotate(sapo, -90)             
                pos_sap_x = pos_sap_x - 70
                sapo_angulo = pygame.transform.rotate(sapo, 90)                         
            if event.key == K_RIGHT:
                pos_sap_x = pos_sap_x + 70
                sapo_angulo = pygame.transform.rotate(sapo, -90)
            if event.key == K_UP:
                pos_sap_y = pos_sap_y - 70
                sapo_angulo = pygame.transform.rotate(sapo, 0)
            if event.key == K_DOWN:
                pos_sap_y = pos_sap_y + 70
                sapo_angulo = pygame.transform.rotate(sapo, -180)
    
    tela.blit(pista, (0,260))
    tela.blit(pista, (0,475))
    tela.blit(rio, (0,40))
    tela.blit(pista, (0,-180))

    if sapo_rect.colliderect(car_1_rect):
        print('Errou')
    

    tela.blit(tronco_1, (pos_tro_1, 45))
    if pos_tro_1 >= largura:
        pos_tro_1 = -250
    pos_tro_1 = pos_tro_1 + 1

    tela.blit(tronco_2, (pos_tro_2, 55))
    if pos_tro_2 >= largura:
        pos_tro_2 = -250
    pos_tro_2 = pos_tro_2 + 1

    tela.blit(tronco_3, (pos_tro_3, 130))
    if pos_tro_3 >= largura:
        pos_tro_3 = -250
    pos_tro_3 = pos_tro_3 + 1.5

    tela.blit(tronco_3, (pos_tro_31, 130))
    if pos_tro_31 >= largura:
        pos_tro_31 = -250
    pos_tro_31 = pos_tro_31 + 1.5

    tela.blit(tronco_2, (pos_tro_21, 130))
    if pos_tro_21 >= largura:
        pos_tro_21 = -250
    pos_tro_21 = pos_tro_21 + 1.5

    tela.blit(pedra, (pos_ped, 200))
    if pos_ped >= largura:
        pos_ped = -250
    pos_ped = pos_ped + 1

    tela.blit(pedra, (pos_ped1, 200))
    if pos_ped1 >= largura:
        pos_ped1 = -250
    pos_ped1 = pos_ped1 + 1

    tela.blit(car_1, (pos_car_1, 265))
    if pos_car_1 >= largura:
        pos_car_1 = -150
    pos_car_1 = pos_car_1 + 1

    tela.blit(car_2, (pos_car_2, 340))
    if pos_car_2 >= largura:
        pos_car_2 = -150
    pos_car_2 = pos_car_2 + 2

    tela.blit(car_3, (pos_car_3, 410))
    if pos_car_3 >= largura:
        pos_car_3 = -150
    pos_car_3 = pos_car_3 + 2
    
    tela.blit(car_4, (pos_car_4, 410))
    if pos_car_4 >= largura:
        pos_car_4 = -150
    pos_car_4 = pos_car_4 + 2

    tela.blit(car_5, (pos_car_5, 265))
    if pos_car_5 >= largura:
        pos_car_5 = -150
    pos_car_5 = pos_car_5 + 1

    sapo_pula = tela.blit(sapo, (pos_sap_x,pos_sap_y))

    #Colisão
    
    # if sapo_pula.Rect.colliderect(car_1):
    #     print('Errou')

    
    
    
    pygame.display.update()