import pygame
import random 
import sys
import math 

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Mi dibujo animado")

rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
cafe = (115, 62, 23)
cafecito = (196, 189, 179)
PI = math.pi
clock = pygame.time.Clock()
fucsia = ( 255, 43, 90)

while True:
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    ventana.fill(negro)
    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta" , 1, rosado)
    ventana.blit(texto,(70,60))
    pygame.display.flip()
    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto2 = fuente_arial.render("Esp. Sistemas" , 1, rosado)
    ventana.blit(texto2,(171,81))
    pygame.display.flip()
    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto3 = fuente_arial.render("Nicolle Daniela Macìas Piracòn" , 0.5, rosado)
    ventana.blit(texto3,(80,470))
    pygame.display.flip()
    pygame.draw.circle(ventana, amarillo, (80,350), 30)

    # Elcuadrado dentro de la ventana que va a tener la figura
    pygame.draw.rect(ventana, blanco, ((50, 100), (400, 350)), 1)

    # El cuadrado relleno del tren
    pygame.draw.rect(ventana, verde, (120, 280, 260, 110))

    # Circulos como llantas
    pygame.draw.circle(ventana, naranja, (160,390), 30)
    pygame.draw.circle(ventana, naranja, (250,390), 30)
    pygame.draw.circle(ventana, naranja, (340,390), 30)

    # Los rectàngulos que unen a las llantas
    pygame.draw.rect(ventana, cafe, (160, 380, 70, 25))
    pygame.draw.rect(ventana, cafe, (260, 380, 80, 25))

    # Cuadrado relleno de la parte de donde va el conductor (rojo)
    pygame.draw.rect(ventana, rojo, (250, 180, 130, 100), 20)

    # El chuchu
    pygame.draw.rect(ventana, azul, (130, 230, 40, 50))

    # Cuadrado arriba del chuchu
    pygame.draw.rect(ventana, cian, (120, 200, 62, 30))

    # Rectàngulo que està arriba del cuadrado rojo
    pygame.draw.rect(ventana, amarillo, (235, 160, 160, 30))

    # La ùltima parte del techo del tren
    pygame.draw.rect(ventana, cafecito, (240, 140, 150, 20))

    # La carita 
    pygame.draw.circle(ventana, fucsia, (315,230), 35)

    # Los ojos de la cara 
    pygame.draw.circle(ventana, blanco, (330,230), 10)
    pygame.draw.circle(ventana, blanco, (300,230), 10)

    # Pupilas de los ojos
    pygame.draw.circle(ventana, cafe, (330,230), 5)
    pygame.draw.circle(ventana, cafe, (300,230), 5)

    # Boca 
    pygame.draw.circle(ventana, rosado, (315,250), 8)

    # Rectàngulos de la parte de adelante
    pygame.draw.rect(ventana, cafecito, (90, 290, 30, 90))
    pygame.draw.rect(ventana, fucsia, (60, 280, 30, 110))

    # Animaciòn 
    for i in range(100):
        pygame.draw.circlecolor_aleatorio= (random.randint(0,255),random.randint(0,255), random.randint(0,255))
        





    pygame.display.flip()
    




