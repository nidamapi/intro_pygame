import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

# Clase que representa un círculo
class Circulo(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)  # Crear una superficie
        pygame.draw.circle(self.image, color, (25, 25), 25)  # Dibujar un círculo
        self.rect = self.image.get_rect()  # Crear el rectángulo para manejar la posición
        self.rect.x = x  # Establecer la posición X inicial
        self.rect.y = y  # Establecer la posición Y inicial

    def update(self):
        self.rect.x += 5  # Mover el círculo hacia la derecha
        if self.rect.x > 800:  # Si el círculo sale de la pantalla, vuelve a la izquierda
            self.rect.x = -50

# Crear grupo de sprites
circulos = pygame.sprite.Group()

# Crear 5 círculos y añadirlos al grupo
for i in range(5):
    color = (pygame.Color(i * 50, 100, 255))  # Colores variados para cada círculo
    circulo = Circulo(color, 100 * (i + 1), 100)  # Posiciones iniciales
    circulos.add(circulo)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar todos los círculos
    circulos.update()

    # Rellenar la pantalla de negro
    pantalla.fill((0, 0, 0))

    # Dibujar todos los círculos en la pantalla
    circulos.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego (60 FPS)
    reloj.tick(60)


### Explicaciòn del juego: Imagina que tienes muchos círculos de colores corriendo por la pantalla. Cada uno tiene su propio color y se mueve de un lado a otro. Si un círculo llega al final de la pantalla, vuelve a empezar desde el principio. Todo esto pasa muy rápido y se repite una y otra vez, como un ciclo infinito. ¡Y eso es todo! El código le dice a los círculos cómo moverse y dibujarse, ¡y nosotros solo tenemos que verlo en la pantalla!