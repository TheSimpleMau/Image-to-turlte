from turtle import Turtle,Screen, colormode
from PIL import Image
from statistics import mode
from time import time

class ImageToTurtle:

    colormode(255)

    def __init__(self,nombre_imagen,zoom):
        self.nombre_imagen = nombre_imagen
        self.zoom = zoom
    

    def point_maker(self,object,color):
        object.pendown()
        object.color(color)
        object.dot(self.zoom)
        object.penup()


    def redimention_image(self):
        im = Image.open(self.nombre_imagen) 
        pix = im.load()
        size = im.size
        print(size)
        if size[0] != size[1] or size[0] > 100:
            im = im.resize((100,100))
            pix = im.load()
            size = im.size
        print(size)
        return pix,size


    def cords_colors(self,size,pix):
        cords_colors = []
        for x in range(0,size[0]):
            for y in range(0,size[1]):
                cords_colors.append(pix[y,x])
        frecuent_color = mode(cords_colors)
        return cords_colors,frecuent_color


    def similar_color(self,frecuent_color):
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
        return similar_color


    def image_maker(self):
        inicio = time()
        pix,size = self.redimention_image()
        cords_colors,frecuent_color = self.cords_colors(size,pix)
        similar_color = self.similar_color(frecuent_color)
        turtle = Turtle(visible=False)
        turtle.shape('turtle')
        turtle.penup()
        turtle.speed(10)
        screen = Screen()
        screen.tracer(False)
        screen.bgcolor(frecuent_color) 
        screen.title("The painter turtle")
        turtle.goto(-(size[0]/2)*(self.zoom),(size[1]/2)*(self.zoom))
        pixel_to_draw = 0
        tiempos_renglones = []
        pixeles_hechos_per_renglon = []
        for i in range(0,size[0]):
            pixel_hecho = 0
            tiempo_renglon_inicio = time()
            for j in range(0,size[1]):
                if cords_colors[pixel_to_draw] in similar_color or cords_colors[pixel_to_draw] == frecuent_color:
                    turtle.forward(self.zoom)
                    pixel_to_draw += 1
                else:
                    self.point_maker(turtle,cords_colors[pixel_to_draw])
                    turtle.forward(self.zoom)
                    pixel_to_draw += 1
                    pixel_hecho += 1
            turtle.backward((size[0]*self.zoom))
            turtle.right(90)
            turtle.forward(self.zoom)
            turtle.left(90)
            tiempo_renglon_fin = time()
            tiempo_renglon = round(tiempo_renglon_fin-tiempo_renglon_inicio,2)
            tiempos_renglones.append(tiempo_renglon)
            pixeles_hechos_per_renglon.append(pixel_hecho)
            if len(tiempos_renglones)%10==0:
                print(f"Quedan {size[0]-len(tiempos_renglones)} por hacer :)")
            screen.update()

        screen.tracer(True)
        turtle.hideturtle() #Para ocultar a la torutga

        fin = time()
        print(f'Tiempo empleado para dibujar: {round((fin-inicio)/60,2)} minutos')
        screen.exitonclick()