# Estructura de un juego en Pygame 

## Inicializaciòn

- Como en todo programa en Python, se debe importar los mòdulos o librerìas a utilizar
`import pygame`

- Inicializar Pygame usando a funciòn init(). Inicializa todos los mòdulos importados.
`pygame.init()`

## Visualizaciòn de la ventana

`ventana = pygame.display.set_mode((600,400))`

- set mode() es la funciòn de definir el tamaño de la ventana. En el ejemplo, se està definiendo una ventana de 600 px de ancho, por 400 px de alto.

`pygame.display.set_caption("Mi ventana")`

- set caption() es la funciòn que añade un tìtulo a la ventana.

### Funciòn set_mode()

`set_mode(size =(0,0), flags = 0, depth = 0, display = 0)`

- size = (600,400) : define el tamaño de la ventana.

- flags = define uno o màs comportamientos para la ventana.
    - Valores:
        - pygame.FULLSCREEN
        - pygame.RESIZABLE
    - Ejemplo:
        - flags = pygame.FUllSCREEN | pygame.RESIZABLE: pantalla completa, dimensiones modificables.

## Bucle del juego - game loop
- Bucle infinito que se interrumpirà al cumplir ciertos criterios.
- Reloj interno del juego
- En cada iteraciòn del bucle del juego podemos mover a un personaje, o tener en cuenta que un objeto ha alcanzado a otro o que se ha cruzado la lìnea de llegada, lo que quiere decir que la partida ha terminado.
- Cada iteraciòn es una oportunidad para actualizar todos los datos relacionados con el estado actual de la partida.
- En cada iteraciòn se realiza las siguientes tareas:
    1. Comprobar que no se alcanzan las condiciones de parada, en cuyo caso se interrumpe el bucle.
    2. Actualizar los recursos necesarios para la iteraciòn actual.
    3. Obtener las entradas del sistema, o de interacciòn con el jugador.
    4. Actualizar todas las entidades que caracterizan el juego.
    5. Refrescar la pantalla.

## Superficies pygame
- Superficie: 
    - Elemento geomètrico.
    - Lìnea, polìgono, imàgen, texto que se muestra en la pantalla.
    - El polìgono se puede o no rellenar de color.
    - Las superficies se crean de diferente manera dependiendo del tipo:
        - imagen: image.load()
        - texto: font.render()
        - Superficie genèrica: pygame.Surface()
        - Ventana del juego: pygamen.display.set_mode()

# Ejemplo: Bandera de Colombia

```python
# importamos la librerìa pygame
import pygame
import random 

# inicializamos los mòdulos de pygame
pygame.init()

#  Establecer tìtulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# Colores de la bandera
amarillo = (255, 255, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)


# crear una superficie
superficie_amarillo = pygame.Surface((400,200))
superficie_azul = pygame.Surface((400, 100))
superficie_rojo = pygame.Surface((400, 100))




# Rellenamos la superficie de color amarillo, azul, rojo
superficie_amarillo.fill(amarillo)
superficie_azul.fill(azul)
superficie_rojo.fill(rojo)

# Inserto o muevo la superficie de la ventana 
ventana.blit(superficie_amarillo, (0,0))
ventana.blit(superficie_azul, (0,200))
ventana.blit(superficie_rojo, (0,300))



# Actualiza la visualizaciòn de la ventana 
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit() ```

```
![Bandera](Bandera.jpg)```

## Gestiòn del tiempo y los eventos

### Mòdulo time

- Ofrece varias funciones que permiten cronometrar la sesiòn actual (desde el init()) o pausar, la ejecuciòn, por ejemplo.
- Funciones:
    - pygame.time.get_ticks
    - pygame.time.waitpygame.time.delay

-  Objeto Clock
    - La funciòn tick permite actualizar el reloj asociado con el juego actual.
    - Se llama cada vez que se actualiza la pantalla del juego.
    - Permite especificar el nùmero màximo de fotogramas que se muestran por segundo, y por tanto, limitar y controlar la velocidad de ejecuciòn del juego.
    - Si insertamos en un bucle de juego la siguiente lìnea, garantizamos que nunca se irà mas ràpido de 50 fotogramas por segundo: `Clock.tick(50)`

### Gestiòn de eventos
- Hay diferentes formas para que el programa sepa que se ha desencadenado un evento.
- Es escencial que los programas puedan conocer inmediatamente las acciones del jugadora a travès del teclado, el mouse, e joystick o cualquier otro perifèrico.

#### Funciòn pygame.event.get
- Permite obtener todos los eventosen espera de ser procesados y que estàn disponibles en una cola.
- Si no hay ninguno, entonces se obtiene una colecciòn vacìa.
```Python
# Usamos un bucle for para recorrer todos los eventos de la colecciòn obtenida al llamar a la funciòn get.
for event in pygame.even.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.k_ESCAPE:
            PARAR_JUEGO = True

```
#### Funciòn pygame.event.wait
- Està funciòn espera a que ocurra un evento, y en cuanto sucede està disponible.

```Python
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
```
#### Funciòn pygame.event.poll
- Devuelve solo uno de los eventos que estàn en la cola de espera.


## Sonidos en Pygame
- pygame.mixer: mòdulo que permite la gestiòn del sonido.
- music: submòdulo que gestiona la mùsica de fondo.Necesariamente solo hay uno a la vez.
- Sound: objeto de mixer, que se puede instanciar varias veces para usarlo en los efectos de sonido del juego.

### Archivos de sonido
- Se recomienda usar dos formatos, principalmente:
    - Formato WAW (Waverform Audio File Format)
    - Formato abierto y gratuito OGG

### Channe (canal) en Pygame
- Un juego tiene varios canales de sonido. 
- Se puede asignar un sonido al canal nùmero 1 y otro diferente al nùmero 2.
- Entonces es posible reproducir sonidos simultàneamente activando la lectura en diferentes canales.

## Sprites
- Objeto que asocia una ubicaciòn, una representaciòn gràfica (esta  aquella imàgen, por ejemplo) y un conjunto de propiedades.
- Estas propiedades pueden ser un nombre, un texto, valores booleanos que caracterizan el objeto en cuestiòn (por ejemplo si el objeto se puede mover o no)
- Una posible traducciòn del tèrmino sprite podrìa ser "imagen-objeto" que se actualiza con cada iteraciòn del bucle del juego.
- Cuanto mas complejo es el juego, màs objetos gràficos tiene que gestionar y actualizar, lo que puede ser tedioso.
- Pygame usa no solo la nociòn de sprite, sino la nociòn de grupo de sprites (group)
- La nociòn de group permite agrupar los objetos del mismo tipo. Ejemplo: todos los soldados de un ejercito, lo que se entiende como una colecciòn de instancias de una clase Soldado.
- Un determinado procesamiento se puede aplicar a un conjunto o subconjunto de sprites. Ejemplo: cambiar el color de todos los enemigos o hacer invisibles algunos objetos.


## Group
- La clase Group de Pygame se utiliza para manejar y organizar múltiples sprites (objetos gráficos) en un solo grupo.
### Clase Group en Pygame
- Agrupación de Sprites: Permite agrupar múltiples sprites del mismo tipo para gestionarlos juntos (por ejemplo, todos los enemigos o todos los proyectiles).
- Procesamiento Colectivo: Puedes aplicar operaciones como actualizar, dibujar o cambiar propiedades a todos los sprites dentro del grupo con una sola línea de código.
- Eficiencia: Facilita la gestión de muchos objetos gráficos, evitando tener que tratar con cada sprite individualmente.

### Métodos Clave:

- add(sprite): Añadir un sprite al grupo.
- update(): Actualizar todos los sprites en el grupo.
- draw(surface): Dibujar todos los sprites sobre una superficie.
- remove(sprite): Eliminar un sprite del grupo.

### Ejemplo de uso:
 Un ejército de enemigos puede ser representado como un solo grupo, permitiendo aplicarles cambios o actualizaciones de forma colectiva (por ejemplo, moverlos o hacerlos invisibles).





