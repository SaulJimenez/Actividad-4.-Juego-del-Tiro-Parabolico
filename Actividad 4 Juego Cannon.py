# Actividad 4 - Juego Cannon.
# Autores: Leonardo Delgado Rios-A00827915, Saul Jimenez Torres-A01283849.
# Aplicacion que desarrolla el minijuego de tiro parabolico. 
# Fecha de ultima modificacion: 10/30/2020.
# Se importan las librerias que se utilizaran para el correcto desarrollo de
# la aplicación.
from random import randrange
from turtle import *
from freegames import vector

# Se establecen los valores defeault para el proyectil, la velocidad y los
# objetivos del juego.
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Funcion tap, funcion que indica la velocidad de nuestro proyectil mientras se
# encuentre en los limites de la ventana.
def tap(x, y):
    "Respond to screen tap."
    # Da lo valores iniciales a nuestro proyectil, para que una vez se realice
    # el clic este salga disparado. 
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 650) / 25
        speed.y = (y + 650) / 25

# Funcion inside, funcion que verifica a través de un valor booleano que los
# objetivos o el proyectil se encuentren dentro de los limites.
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def redraw(z):
    goto(z.x, z.y)
    dot(20, 'blue')
    update()

# Funcion draw, funcion cuya funcionalidad es dibujar los objetivos y el
# proyectil para el desarrollo del juego.
def draw():
    "Draw ball and targets."
    clear()
    # Mientras nuestra lista de objetivos cuente con un valor diferente de null
    # se dibujaran los objetivos.
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    
    # Mientras el valor booleano sea verdadero, es decir, mientras se encuentre
    # dentro de la ventana dibujara nuestro proyectil.
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Funcion move, funcion que agrega los objetivos a nuestra lista para dibujar,
# les da un movimiento para que se desplacen de derecha a izquierda, ademas de
# eliminar los objetivos que ya han sido "explotados" y dar esa fuerza similar
# a la gravedad a nuestro proyectil, para que tenga su forma parabolica.
def move():
    "Move ball and targets."
    # Agrega los objetivos a nuestra lista definida al inicio del codigo, con
    # valor de la coord x = 200, y un valor de y aleatorio de -150 a 150.
    if randrange(150) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    
    # Desplaza los objetivos agregados a la lista -5 en la coord x cada que se
    # realiza la iteración.
    for target in targets:
        target.x -= 5
    
    # Verifica que mientras el proyectil se encuentre en la ventana, este tenga
    # cierta caida en la coord y, para simular la fuerza de la gravedad.
    if inside(ball):
        speed.y -= 1.5
        ball.move(speed)
    
    # Realiza una variable auxiliar de la lista creada al inicionde la funcion
    # y limpia los valores que dicha lista contenia.
    dupe = targets.copy()
    targets.clear()
    
    # Verifica que objetivos no se han explotado todavia, y los regresa
    # nuevamente a la lista targets definida al inicio del codigo.
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    
    # Manda a llamar a la funcion antes definida para dibujar a los objetivos.
    draw()
    
    # Verifica que los objetivos se encuentren dentro de la ventana con un
    # booleano, en caso de no encontrarse dentro, modifica su coord x para
    # reposicionarse en la coord x = 200, es decir, lado derecho de la ventana.
    for target in targets:
        if not inside(target):
            target.x = 200
            redraw(target)
    
    ontimer(move, 50)

# Aqui se definen las caracterisiticas de la ventana donde se desarrolla el
# codigo y se manda a llamar las funciones necesarias para dar inicio al juego.
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()