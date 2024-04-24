# Solicitar datos generales del niño
nombre = input("Ingrese el nombre del niño: ")
edad = int(input("Ingrese la edad del niño: "))

# Mostrar opciones de colores favoritos
print("Seleccione el color favorito del niño:")
print("1. Rojo")
print("2. Azul")
print("3. Verde")
print("4. Amarillo")
print("5. Rosa")

# Solicitar selección de color favorito
opcion_color = int(input("Ingrese el número correspondiente al color favorito: "))

# Asignar color favorito basado en la selección del usuario
colores = {1: "Red", 2: "blue", 3: "green", 4: "yellow", 5: "pink"}
color_favorito = colores.get(opcion_color)

# Mostrar los datos almacenados
print("\nDatos del niño:")

#menu
def menu():
    print("1. ¿Quién es copito?" , "2. Su mejer amigo" , "3. Les gusta jugar" , "4. Sale el sol" , "5. Todos a salvo " , sep= "\n")
opción = input("Ingrese el número de secuencia: ")

import turtle
match opción:
    case "1":

        turtle.bgcolor("sky blue")

        #cuadro texto (titulo)
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, 290)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
    
        turtle.setpos(-330, 250)
        turtle.write("¿Quién es Copito?" , font=("Arial" , 14 , "normal"))
        turtle.end_fill()
        
        #cuadro texto (escena)
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, -150)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(150)
            turtle.right(90)

        turtle.setpos(-330, -255)
        turtle.write("Había una vez un muñeco de nieve, lindo y muy amigable llamado Copito de" + str(edad) + "años que \n disfrutaba de salir a jugar, hacer amigos y explorar los paisajes nevados del invierno. \n Con su sonrisa radiante y sus ojos brillantes, siempre contagiaba alegría a quienes lo rodeaban. \n No importaba cuán frío estuviera afuera, Copito siempre encontraba la manera de \n derretir los corazones con su calidez." , font=("Arial" , 12 , "normal"))

        turtle.end_fill()

        turtle.penup()
        turtle.home()
        turtle.setpos(-50, 60)
        turtle.speed(3)

        #paralelogramo (sombrero)
        turtle.pendown()
        turtle.fillcolor(color_favorito)
        turtle.begin_fill()
        for x in range(0, 2):
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(60)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(10)

        #cuadrado pequeño (cabeza)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(75)
            turtle.right(90)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(-24)
        turtle.right(120)
        turtle.forward(30)

        #triangulo pequeño (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(-35)
        turtle.right(90)

        #cuadrado garnde (cuerpo)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()

        turtle.forward(-45)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(-90)
        turtle.fd(-115)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(90)
        turtle.fd(70)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.fd(30)

        #circulo (botones)
        turtle.pendown()
        r = 10
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(40)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(120)

        #circulos pequeños (ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(2)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.exitonclick()

    case "2":
        turtle.bgcolor("sky blue")

        #cuadro texto (titulo)
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, 290)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
    
        turtle.setpos(-330, 250)
        turtle.write("Su mejor amigo" , font=("Arial" , 14 , "normal"))
        turtle.end_fill()
        
        #cuadro texto
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, -150)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(150)
            turtle.right(90)
        turtle.end_fill()

        #texto
        turtle.penup()
        turtle.setpos(-330, -250)
        turtle.pendown()
        turtle.write("En una de sus aventuras, se encontró con un pequeño pingüino" + "*" + nombre + "*" + ".Este era alguien \n extrovertido, de corazón de oro y lleno de energía. Mientras que el muñeco de nieve era \n tranquilo pero juguetón, social, cariñoso e inocente, características que son hermosas y \n admirables. Juntos formaron una amistad sólida, compartiendo risas y momentos inolvidables." , font=("Arial" , 12 , "normal"))
        
        turtle.penup()
        turtle.home()
        turtle.setpos(-170, 60)
        turtle.speed(3)

        #muñeco de nieve
        #paralelogramo (sombrero)
        turtle.pendown()
        turtle.fillcolor(color_favorito)
        turtle.begin_fill()
        for x in range(0, 2):
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(60)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(10)

        #cuadrado pequeño (cabeza)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(75)
            turtle.right(90)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(-24)
        turtle.right(120)
        turtle.forward(30)

        #triangulo pequeño (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(-35)
        turtle.right(90)

        #cuadrado garnde (cuerpo)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()

        turtle.forward(-45)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(-90)
        turtle.fd(-115)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(90)
        turtle.fd(70)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.fd(30)

        #circulo (botones)
        turtle.pendown()
        r = 10
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(40)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(120)

        #circulos pequeños (ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(2)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()
        turtle.penup()
        turtle.setpos(70, 10)

        #pinguino
        #circulos (cabeza)
        turtle.home()
        turtle.penup()
        turtle.setpos(80, 10)

        turtle.pendown()
        r = 50
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        r1 = 40
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #cirulos (cuerpo)
        r2 = -60
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r2)
        turtle.end_fill()

        r3 = -50
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r3)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(30)
        turtle.right(120)

        #Triangulo (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(-20)

        #circulos(ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(25)
        turtle.right(90)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #rombo (pies)
        turtle.penup()
        turtle.setpos(90, -110)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.home()
        turtle.setpos(50, -110)
        turtle.right(90)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()

        turtle.exitonclick()
        
    case "3":

        turtle.bgcolor("sky blue")

        #cuadro texto (titulo)
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, 290)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
    
        turtle.setpos(-330, 250)
        turtle.write("Les gusta jugar" , font=("Arial" , 14 , "normal"))
        turtle.end_fill()
        
        turtle.penup()
        turtle.home()
        turtle.setpos(-190, 90)
        turtle.speed(3)
        
        #muñeco de nieve
        #paralelogramo (sombrero)
        turtle.pendown()
        turtle.fillcolor(color_favorito)
        turtle.begin_fill()
        for x in range(0, 2):
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(60)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(10)

        #cuadrado pequeño (cabeza)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(75)
            turtle.right(90)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(-24)
        turtle.right(120)
        turtle.forward(30)

        #triangulo pequeño (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(-35)
        turtle.right(90)

        #cuadrado garnde (cuerpo)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()

        turtle.forward(-45)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(-90)
        turtle.fd(-115)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(90)
        turtle.fd(70)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.fd(30)

        #circulo (botones)
        turtle.pendown()
        r = 10
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(40)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(120)

        #circulos pequeños (ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(2)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()
        turtle.penup()
        turtle.setpos(70, 10)

        #pinguino
        #circulos (cabeza)
        turtle.home()
        turtle.penup()
        turtle.setpos(140, 20)

        turtle.pendown()
        r = 50
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        r1 = 40
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #cirulos (cuerpo)
        r2 = -60
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r2)
        turtle.end_fill()

        r3 = -50
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r3)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(30)
        turtle.right(120)

        #Triangulo (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(-20)

        #circulos(ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(25)
        turtle.right(90)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #rombo (pies)
        turtle.penup()
        turtle.setpos(145, -100)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.home()
        turtle.setpos(105, -100)
        turtle.right(90)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()
        
        #circulo (pelota)
        turtle.penup()
        turtle.home()
        turtle.setpos(0, -100)
        
        turtle.pendown()
        r4 = 35
        turtle.fillcolor("purple")
        turtle.begin_fill()
        turtle.circle(r4)
        turtle.end_fill()

        #cuadro texto
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, -150)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(150)
            turtle.right(90)
        turtle.end_fill()

        #texto
        turtle.penup()
        turtle.setpos(-330, -230)
        turtle.pendown()
        turtle.write("Un día, los dos amigos decidieron que querían jugar pelota ya que estaban aburridos. \n Se divirtieron durante horas, disfrutando de la compañía y la emoción del juego bajo el \n brillante sol invernal." , font=("Arial", 12 , "normal"))

        turtle.exitonclick()

    case "4":

        turtle.bgcolor("sky blue")

#cuadro texto (titulo)
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, 290)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
    
        turtle.setpos(-330, 250)
        turtle.write("Sale el sol" , font=("Arial" , 14 , "normal"))
        turtle.end_fill()
        
        turtle.penup()
        turtle.home()
        turtle.setpos(-170, 60)
        turtle.speed(3)
        
        #muñeco de nieve
        #paralelogramo (sombrero)
        turtle.pendown()
        turtle.fillcolor(color_favorito)
        turtle.begin_fill()
        for x in range(0, 2):
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(60)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(10)

        #cuadrado pequeño (cabeza)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(75)
            turtle.right(90)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(-24)
        turtle.right(120)
        turtle.forward(30)

        #triangulo pequeño (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(-35)
        turtle.right(90)

        #cuadrado garnde (cuerpo)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()

        turtle.forward(-45)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(-90)
        turtle.fd(-115)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(90)
        turtle.fd(70)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.fd(30)

        #circulo (botones)
        turtle.pendown()
        r = 10
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(40)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(120)

        #circulos pequeños (ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(2)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()
        turtle.penup()
        turtle.setpos(70, 10)

        #pinguino
        #circulos (cabeza)
        turtle.home()
        turtle.penup()
        turtle.setpos(80, 10)

        turtle.pendown()
        r = 50
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        r1 = 40
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #cirulos (cuerpo)
        r2 = -60
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r2)
        turtle.end_fill()

        r3 = -50
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r3)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(30)
        turtle.right(120)

        #Triangulo (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(-20)

        #circulos(ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(25)
        turtle.right(90)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #rombo (pies)
        turtle.penup()
        turtle.setpos(90, -100)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.home()
        turtle.setpos(50, -100)
        turtle.right(90)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()

        #circulo (pelota)
        turtle.penup()
        turtle.home()
        turtle.setpos(120, -100)
        
        turtle.pendown()
        r4 = 35
        turtle.fillcolor("purple")
        turtle.begin_fill()
        turtle.circle(r4)
        turtle.end_fill()

        #cuadro texto
        turtle.penup()
        turtle.home()
        turtle.setpos(-345, -150)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(150)
            turtle.right(90)
        turtle.end_fill()

        #texto
        turtle.penup()
        turtle.setpos(-330, -250)
        turtle.pendown()
        turtle.write("Pero a medida que el día avanzaba, el sol comenzó a calentar intensamente. Copito se dio \n cuenta de que empezaba a derretirse lentamente, y el pingüinito sabía que no podría soportar \n el calor por mucho tiempo. Con preocupación, buscaron desesperadamente refugio para \n protegerse del derretimiento y mantenerse a salvo." , font=("Arial" , 12 , "normal"))

        turtle.exitonclick()

    case "5":

        turtle.bgcolor("sky blue")
        #cuadro texto (titulo)
        turtle.penup()
        turtle.home()
        turtle.setpos(-170, 290)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(680)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
    
        turtle.setpos(-165, 250)
        turtle.write("Todos a salvo" , font=("Arial" , 14 , "normal"))
        turtle.end_fill()
        
        turtle.penup()
        turtle.home()
        turtle.speed(3)
        
        #sol
        # Definir el tamaño de la pantalla
        pantalla = turtle.Screen()
        pantalla.setup(width=800, height=600)
        pantalla.bgcolor("lightblue")

        # Crear el objeto tortuga
        tortuga = turtle.Turtle()
        tortuga.speed(0)
        tortuga.pensize(5)

        # Dibujar el círculo central del sol
        tortuga.penup()
        tortuga.goto(-293, 175)
        tortuga.pendown()
        tortuga.fillcolor("yellow")
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()

        # Dibujar los rayos del sol
        tortuga.penup()
        tortuga.goto(-300, 150)
        tortuga.setheading(0)

        for i in range(36):
            tortuga.pendown()
            tortuga.forward(100)
            tortuga.penup()
            tortuga.backward(87)
            tortuga.left(10)

        #arbol
        turtle.penup()
        turtle.setpos(-170, 145)

        turtle.pendown()
        turtle.fillcolor("light green")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(100)
            turtle.left(120)

        turtle.end_fill()

        turtle.penup()
        turtle.forward(-10)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(-90)

        turtle.pendown()
        turtle.fillcolor("light green")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(120)
            turtle.left(120)

        turtle.end_fill()

        turtle.penup()
        turtle.forward(-15)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(-90)

        turtle.pendown()
        turtle.fillcolor("light green")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(150)
            turtle.left(120)

        turtle.end_fill()

        turtle.penup()
        turtle.forward(45)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(-90)

        turtle.pendown()
        turtle.fillcolor("brown")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(60)
            turtle.right(90)

        turtle.end_fill()

        turtle.penup()
        turtle.setpos(-5, 60)
        
        #muñeco de nieve
        #paralelogramo (sombrero)
        turtle.pendown()
        turtle.fillcolor(color_favorito)
        turtle.begin_fill()
        for x in range(0, 2):
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(60)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(10)

        #cuadrado pequeño (cabeza)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(75)
            turtle.right(90)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(-24)
        turtle.right(120)
        turtle.forward(30)

        #triangulo pequeño (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(-35)
        turtle.right(90)

        #cuadrado garnde (cuerpo)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()

        turtle.forward(-45)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(-90)
        turtle.fd(-115)
        turtle.right(-90)
        turtle.fd(-100)
        turtle.right(90)
        turtle.fd(70)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.fd(30)

        #circulo (botones)
        turtle.pendown()
        r = 10
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(40)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(120)

        #circulos pequeños (ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(2)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()
        turtle.penup()
        turtle.setpos(70, 10)

        #pinguino
        #circulos (cabeza)
        turtle.home()
        turtle.penup()
        turtle.setpos(160, 10)

        turtle.pendown()
        r = 50
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

        r1 = 40
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #cirulos (cuerpo)
        r2 = -60
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r2)
        turtle.end_fill()

        r3 = -50
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(r3)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-120)
        turtle.forward(30)
        turtle.right(120)

        #Triangulo (nariz)
        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for x in range(0, 3):
            turtle.forward(25)
            turtle.right(120)

        turtle.end_fill()

        turtle.penup()
        turtle.right(90)
        turtle.forward(-20)

        #circulos(ojos)
        turtle.pendown()
        r1 = 5
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        turtle.penup()
        turtle.right(-90)
        turtle.forward(25)
        turtle.right(90)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r1)
        turtle.end_fill()

        #rombo (pies)
        turtle.penup()
        turtle.setpos(180, -100)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()

        turtle.penup()
        turtle.home()
        turtle.setpos(120, -100)
        turtle.right(90)

        turtle.pendown()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.left(60)
        for x in range(0, 2):
            turtle.forward(15)
            turtle.left(60)
            turtle.forward(15)
            turtle.left(120)
        turtle.end_fill()

        #cuadro texto
        turtle.penup()
        turtle.home()
        turtle.setpos(-400, -150)
        turtle.speed(10)

        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for x in range(0, 4):
            turtle.forward(800)
            turtle.right(90)
            turtle.forward(150)
            turtle.right(90)
        turtle.end_fill()

        #texto
        turtle.penup()
        turtle.setpos(-380, -260)
        turtle.pendown()
        turtle.write("Finalmente, encontraron un árbol lleno que les ofrecía sombra y frescura. Aliviados, se refugiaron debajo de sus \n ramas y buscaron otras formas de divertirse juntos. Desde contar historias hasta jugar juegos de sombras, \n los dos amigos encontraron la manera de disfrutar el resto del día mientras esperaban el frescor de la noche. \n Con sus lazos de amistad más fuertes que nunca, se prometieron seguir explorando y creando recuerdos \n inolvidables juntos. Y así, su historia de amistad continuó floreciendo. Fin!" , font=("Arial" , 12 , "normal"))

        turtle.exitonclick()

turtle.done()