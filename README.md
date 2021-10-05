# Image to Turtle 🐢

Image to Turtle es un programa que, dada una imagen en JPG, la "pintará" con ayuda del modulo Turtle que incluye python.

## Installation 🦦

Para instalarla, bastará con descargar este repositorio. Esto lo puede hacer con el siguiente comando:

```bash
git clone https://github.com/TheSimpleMau/Image-to-turtle.git
```

## Uso 🧑‍💻

Para empezar, tendrá que acceder al archivo main y cambiar (en la linea 4) el nombre de la imagen que quiera que reciba como entrada, es decir, algo como lo siguiente:
```python
imagen = ImageToTurtle('Imagen_de_prueba.jpg',5) #El número 5 es para el zoom que
#quiera que se le aplique a la imagen
```

## Detalles e inconvenientes 😓

Este programa solamente puede realizar imagenes que sea cuadradas y menores a 100x100 pixeles, esto ultimo por la cantidad de tiempo que se tardaría en renderizar la imagen en la ventana de Turtle.

## Contribuciones ✋
Si piensa que existe una mejor manera de optimizar el proceso de renderizado de la imagen en Turtle, se aceptan pull requests :)