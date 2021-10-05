from turtle import Turtle,Screen, colormode
from PIL import Image
from statistics import mode
from time import time

inicio = time()
im = Image.open('./tux_redimension.jpg') # Can be many different formats.
pix = im.load()
# print(im.size)  # Get the width and hight of the image for iterating over
size = im.size

if size[0] != size[1]:
    if (size[0] or size[1]) >= 50:
        if size[0] < size[1]:
            im = im.resize(size[1],size[1])
            size = im.size
        else:
            im = im.resize(size[0],size[0])
            size = im.size
    else:
        if size[0] < size[1]:
            im = im.resize(size[1]/5,size[1]/5)
            size = im.size
        else:
            im = im.resize(size[0]/5,size[0]/5)
            size = im.size

# print(pix[10,10])  # Get the RGBA Value of the a pixel of an image
cords_colors = []
for x in range(0,size[0]):
    for y in range(0,size[1]):
        cords_colors.append(pix[y,x])
frecuent_color = mode(cords_colors)
# print(frecuent_color)
# print(set(cords_colors))
similar_color = []
for sc in range(1,101):
    tone_r = [frecuent_color[0]+sc,frecuent_color[0]-sc]
    for rr in tone_r:
        for sc2 in range(1,101):
            tone_g = [frecuent_color[1]+sc,frecuent_color[1]-sc2]
            for gg in tone_g:
                for sc3 in range(1,101):
                    tone_b = [frecuent_color[2]+sc,frecuent_color[2]-sc3]
                    for bb in tone_b:
                        similar_color.append((rr,gg,bb))
similar_color = list(set(similar_color))
# print(similar_color)
    # similar_color.append([frecuent_color[0],frecuent_color[1],tone_r_menor])
    # similar_color.append([frecuent_color[0],frecuent_color[1],tone_M])


colormode(255)

# rectangle_colors = []
# j = 0
# for i in range(0,size[0]):
#     n=0
#     kola = []
#     while n < size[0]-1:
#         kola.append(cords_colors[j])
#         n+=1
#         j+=1
#     rectangle_colors.append(kola)


#Ir adelante de la lista
# for lista_linea in rectangle_colors:
#     j = len(lista_linea)
#     comparador = []
#     for i in lista_linea:
#         pass
#     pass

# anterioro = 0
# jeje = 0
# for lista_linea in rectangle_colors:
    ##Coso marco##
    # nueva_lista = []
    # i = 0 
    # while i < max(rectangle_colors):
    #     nueva_lista.append([i,rectangle_colors.count(i)])
    #     i += 1
    ##############
    # for pixel_color in lista_linea:
    #     jeje +=1
    #     anterioro = tuple(pixel_color)
    #     if anterioro == lista_linea[jeje]:
    #         pass
    # pass


def rectangle_pixel(lista,indice):
    try:
        value_i = lista[indice]
        new_indice = indice + 1
        counter = 1
        while value_i == lista[new_indice] and new_indice < len(lista)-1:
            # if new_indice < len(lista)-1:
            counter+=1
            new_indice+= 1
            # else:
            #     cola = new_list.append(value_i,counter)
            #     return cola
    except IndexError:
        return None
    return [value_i,counter]

# def width_rectangle_pixel(lista,indice):
#     value_i = lista[indice]
#     new_indice = indice + 1
#     counter = 1
#     while value_i == lista[new_indice] and new_indice < len(lista)-1:
#         # if new_indice < len(lista)-1:
#         counter+=1
#         new_indice+= 1
#         # else:
#         #     cola = new_list.append(value_i,counter)
#         #     return cola
#     new_list = [value_i,counter]
#     return new_list


# print(nueva_lista)
# stop = input()


def point_maker(object,color,zoom):
    object.pendown()
    object.color(color)
    object.dot(zoom)
    object.penup()


def square_maker(object,color,zoom):
    object.pendown()
    object.color(color)
    object.begin_fill()
    for _ in range(0,4):
        object.forward(zoom)
        object.right(90)
    object.end_fill()
    object.penup()

def rectangle_maker(object,color_and_width,zoom):
    object.pendown()
    object.color(color_and_width[0])
    object.begin_fill()
    for _ in range(0,2):
        object.forward(color_and_width[1]*zoom)
        object.right(90)
        object.forward(zoom)
        object.right(90)
    # object.forward(color_and_width[1]*zoom)
    # object.right(90)
    # object.forward(zoom)
    # object.right(90)
    # object.forward(color_and_width[1]*zoom)
    # object.right(90)
    # object.forward(zoom)
    # object.right(90)
    object.forward(color_and_width[1]*zoom)
    object.end_fill()
    object.penup()

zoom = 5
turtle = Turtle()
turtle.shape('turtle')
turtle.penup()
turtle.speed(10)
pantalla = Screen()
pantalla.bgcolor(frecuent_color) #frecuent_color
pantalla.title("The painter turtle")
# pantalla.screensize(size[0],size[1])
# pantalla.setup(width=size[0]*(zoom*3),height=size[1]*(zoom*3))
# turtle.goto(-(size[0]*zoom),size[1]*zoom)
turtle.goto(-(size[0]/2)*(zoom),(size[1]/2)*(zoom))


# print(size[0]*zoom)
xd = 0
tiempos_renglones = []
pixeles_hechos_per_renglon = []
for i in range(0,size[0]):
    pixel_hecho = 0
    tiempo_renglon_inicio = time()
    for j in range(0,size[1]):
        if cords_colors[xd] in similar_color or cords_colors[xd] == frecuent_color:
            turtle.forward(zoom)
            xd += 1
        else:
            point_maker(turtle,cords_colors[xd],zoom)
            turtle.forward(zoom)
            xd += 1
            pixel_hecho += 1
    turtle.backward((size[0]*zoom))
    turtle.right(90)
    turtle.forward(zoom)
    turtle.left(90)
    tiempo_renglon_fin = time()
    tiempo_renglon = round(tiempo_renglon_fin-tiempo_renglon_inicio,2)
    tiempos_renglones.append(tiempo_renglon)
    pixeles_hechos_per_renglon.append(pixel_hecho)
    print(tiempo_renglon)


################################################
######FUNICION QUE FUNCIONA MAS O MENOS XD######
################################################
# xd = 0

# print(size[0])
# tamano_y = 0
# print(frecuent_color)
# while tamano_y < size[1]:
#     tamano_x = 0
#     while tamano_x < size[0]:
#         print(tamano_x)
#         print(round(turtle.xcor(),0),round(turtle.ycor(),0))
#         if xd < len(cords_colors):
#             if cords_colors[xd] != frecuent_color:
#                 is_rectangle = rectangle_pixel(cords_colors,xd)
#                 print(is_rectangle)
#                 if is_rectangle == None:
#                     print('hola')
#                     square_maker(turtle,cords_colors[xd],zoom)
#                     turtle.forward(zoom)
#                     xd+=1
#                     tamano_x+=1
#                 else:
#                     if is_rectangle[1] == 1:
#                         print('hola2')
#                         square_maker(turtle,cords_colors[xd],zoom)
#                         turtle.forward(zoom)
#                         xd+=1
#                         tamano_x+=1
#                     else:
#                         print('hola3')
#                         rectangle_maker(turtle,is_rectangle,zoom)
#                         turtle.forward(is_rectangle[1])
#                         xd+=is_rectangle[1]
#                         tamano_x+=is_rectangle[1]
#             else:
#                 print('hola4')
#                 turtle.forward(zoom)
#                 xd+=1
#                 tamano_x+=1
#     print('hola5')
#     turtle.backward((size[0]*zoom)+zoom+3)
#     turtle.right(90)
#     turtle.forward(zoom)
#     turtle.left(90)
#     tamano_y+=1

######################################################
######FIN DE FUNCION QUE FUNCIONA MAS O MENOS XD######
######################################################




# for kk in range(0,size[0]):
#     for aa in range(0,size[1]):
#         print(turtle.xcor(),turtle.ycor())
#         if xd < len(cords_colors):
#             if cords_colors[xd] != frecuent_color:
#                 is_rectangle = rectangle_pixel(cords_colors,xd)
#                 if is_rectangle == None:
#                     print('hola')
#                     square_maker(turtle,cords_colors[xd],zoom)
#                     turtle.forward(zoom)
#                     xd+=1
#                 else:
#                     if is_rectangle[1] == 1:
#                         print('hola2')
#                         square_maker(turtle,cords_colors[xd],zoom)
#                         turtle.forward(zoom)
#                         xd+=1
#                     else:
#                         print('hola3')
#                         rectangle_maker(turtle,is_rectangle,zoom)
#                         turtle.forward(zoom)
#                         xd+=is_rectangle[1]
#             else:
#                 print('hola4')
#                 turtle.forward(zoom)
#                 xd+=1
        # if cords_colors[xd]==frecuent_color:
        #     turtle.forward(zoom)
        #     xd+=1
        # else:
        #     if xd-1 != len(cords_colors):
        #         ancho_pixel = rectangle_pixel(cords_colors,xd)
        #         print(ancho_pixel)
        #         if ancho_pixel == None:
        #             square_maker(turtle,cords_colors[xd],zoom)
        #             turtle.forward(zoom)
        #             xd+=1
        #         else:
        #             if ancho_pixel[1] > 1:
        #                 rectangle_maker(turtle,ancho_pixel,zoom)
        #                 xd+=ancho_pixel[1]
        #             else:
        #                 square_maker(turtle,cords_colors[xd],zoom)
        #                 turtle.forward(zoom)
        #                 xd+=1
        #         # if ancho_pixel != None:
        #         #     print('hola')
        #         #     if ancho_pixel[1] > 1:
        #         #         print('hola2')
        #         #         rectangle_maker(turtle,ancho_pixel,zoom)
        #         #         xd+=ancho_pixel[1]
        #         #         # rectangle_maker(turtle,ancho_pixel,zoom)
        #         #         # turtle.forward(zoom)
        #         #         # xd+=zoom
        #         # else:
        #         #     print('hola3')
        #         #     square_maker(turtle,cords_colors[xd],zoom)
        #         #     turtle.forward(zoom)
        #         #     xd+=1
        #     else:
        #         square_maker(turtle,cords_colors[xd],zoom)
    # turtle.backward(size[0]*zoom)
    # turtle.right(90)
    # turtle.forward(zoom)
    # turtle.left(90)


turtle.hideturtle() #Para ocultar a la torutga


# pix[10,10] = (255,255,0)  # Set the RGBA Value of the image (tuple)
# im.save('tux-1.png')  # Save the modified pixels as .png


fin = time()
print(f'Tiempo empleado: {fin-inicio}')
pantalla.exitonclick()