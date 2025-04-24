import pygame
import sys

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

# Clase Sprite
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamaño del sprite
        self.image.fill((0, 255, 0))  # Color verde
        self.rect = self.image.get_rect()  # Rectángulo que determina la posición
        self.rect.center = (400, 300)  # Posición inicial

    def update(self):
        keys = pygame.key.get_pressed()  # Detectar las teclas presionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Crear grupo de sprites y añadir el jugador
jugador = Jugador()
sprites = pygame.sprite.Group()  # Grupo para manejar múltiples sprites
sprites.add(jugador)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar todos los sprites
    sprites.update()

    # Dibujar todo en la pantalla
    pantalla.fill((0, 0, 0))  # Fondo negro
    sprites.draw(pantalla)  # Dibujar los sprites en pantalla

    pygame.display.flip()  # Actualizar pantalla
    reloj.tick(60)  # Mantener 60 FPS


# Explicaciòn del juego: Imagina que tienes un cuadrado verde que es tu "jugador". Tú controlas a este cuadrado con las flechas del teclado, y se mueve por la pantalla hacia donde tú quieras. ¡Es como si estuvieras jugando con un cuadrado que se mueve por todo el lugar!
