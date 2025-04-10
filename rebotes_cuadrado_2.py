import pygame
import sys
import random

rojo = (255, 0, 0)
negro = (0, 0, 0)
amarillo = (255, 250, 0)
morado = (250, 0, 250)
verde = (0, 255, 0)


pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("El cuadrado que rebota")
clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 10
YY = 300
MOVIMIENTOY = 10

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)

    XX = XX + MOVIMIENTO
    if XX >= 450:
        XX = 450
        MOVIMIENTO = -10
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 10

    YY = YY + MOVIMIENTOY
    if YY >= 450:
        YY = 450
        MOVIMIENTOY = -10
    elif YY <= 0:
        YY = 0
        MOVIMIENTOY = 10

    pygame.draw.rect(ventana, rojo, (XX, 1, 50, 50))
    pygame.draw.rect(ventana, verde, (XX, 450, 50, 50))
    pygame.draw.rect(ventana, morado, (1, YY, 50, 50))
    pygame.draw.rect(ventana, amarillo, (450, YY, 50, 50))

    color_aleatorio = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(ventana, color_aleatorio, (200, 200, 100, 100))

    pygame.display.flip()
