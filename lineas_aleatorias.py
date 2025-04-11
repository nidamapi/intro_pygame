import pygame
import random 
import sys
import math 


pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Ejercicio")



blanco = (255,255,255)
negro = (0,0,0)
clock = pygame.time.Clock()
verde = (0,255,0)
azul = (0,0,255)
rosado =(255,192,203)


while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)
    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta" , 1, blanco)
    ventana.blit(texto,(70,60))
    pygame.display.flip()
    texto2 = fuente_arial.render("Esp. Sistemas" , 1, blanco)
    ventana.blit(texto2,(170,80))
    texto3 = fuente_arial.render("Nicolle Daniela Macìas Piracòn" , 0.5, blanco)
    ventana.blit(texto3,(80,470))
    
    
    pygame.draw.rect(ventana, verde, ((50, 100), (400, 350)), 1)

    for i in range(100):

        loco1 = random.randint(50,450)
        loco2 = random.randint(100,450)
        loco3 = random.randint(50, 450)
        loco4 = random.randint(100,450)

        color_aleatorio= (random.randint(0,255),random.randint(0,255), random.randint(0,255))


        pygame.draw.line(ventana, color_aleatorio,(loco1, loco2), (loco3, loco4))
    
    pygame.display.flip()