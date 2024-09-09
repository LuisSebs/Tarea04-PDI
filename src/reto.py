import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageStat

def promedio(r, g, b):
    # Calcular el promedio de los tres canales RGB
    promedio = (r + g + b) // 3
    return promedio

def is_grande(num1, num2, porcentaje):
    """
    Verifica si num2 es al menos X% más grande que num1.
    
    :param num1: El número base.
    :param num2: El número a comparar.
    :param porcentaje: El porcentaje mínimo de incremento que debe cumplir num2 respecto a num1.
    :return: True si num1 es al menos X% más grande que num2, False en caso contrario.
    """
    # Calcular el valor de num2 incrementado en X%
    valor_esperado = int(num2 * (1 + porcentaje / 100))
    # Verificar si num2 es mayor o igual al valor esperado
    return num1 >= int(valor_esperado)

def is_menor(num1, num2, porcentaje):
    """
    Verifica si num2 es al menos X% más pequeño que num1.
    
    :param num1: El número base.
    :param num2: El número a comparar.
    :param porcentaje: El porcentaje mínimo de reducción que debe cumplir num2 respecto a num1.
    :return: True si num1 es al menos X% más pequeño que num2, False en caso contrario.
    """
    # Calcular el valor de num2 reducido en X%
    valor_esperado = int(num2 * (1 - porcentaje / 100))
    
    # Verificar si num1 es menor o igual al valor esperado
    return num1 <= int(valor_esperado)

def obtener_region_alrededor(imagen, x, y, ancho_c, alto_c):
    """
    Obtiene una región alrededor del píxel central (x, y) de tamaño (ancho_c)x(alto_c).
    
    :param imagen: La imagen de la que se obtendrán los píxeles.
    :param x, y: Coordenadas del píxel central.
    :param ancho_c: El ancho del área a recortar.
    :param alto_c: El alto del área a recortar.
    :return: Una imagen recortada de la región.
    """
    # Definir las coordenadas del área a recortar (centrado en el píxel (x, y))
    left = x - ancho_c // 2
    top = y - alto_c // 2
    right = x + ancho_c // 2
    bottom = y + alto_c // 2
    
    # Recortar la región alrededor del píxel central
    return imagen.crop((left, top, right, bottom))

def color_promedio(imagen: Image):
    """
        Implementacion con Pillow
    """
    stat = ImageStat.Stat(imagen)
    return tuple(map(int, stat.mean[:3]))

def pasada1(imagen: Image):

    pixeles_marca_de_agua = set()
    pixeles_ceranos_al_blanco = set()
    pixeles_no_cercanos_al_blanco = set()

    factor = 10

    ancho, alto = imagen.size

    nueva_imagen = Image.new('RGB', imagen.size)

    for x in range(ancho):
        for y in range(alto):
            r,g,b = imagen.getpixel((x,y))
            if is_grande(r,g,factor) and is_grande(r,g,factor):
                pixeles_marca_de_agua.add((x,y))             
                p = promedio(r,g,b)
                # Los pixeles cercanos al blanco
                if p > 178:
                    pixeles_ceranos_al_blanco.add((x,y))
                    nueva_imagen.putpixel((x,y),(255,255,255))
                else:
                    pixeles_no_cercanos_al_blanco.add((x,y))
                    nueva_imagen.putpixel((x,y), (r,g,b))
            else:
                nueva_imagen.putpixel((x,y), (r,g,b))

    return nueva_imagen, pixeles_marca_de_agua, pixeles_ceranos_al_blanco, pixeles_no_cercanos_al_blanco

def pasada2(imagen: Image, pixeles):

    pixeles_falla = set()

    ancho, alto = imagen.size

    nueva_imagen = Image.new('RGB', imagen.size)
    
    for x in range(ancho):
        for y in range(alto):
            r,g,b = imagen.getpixel((x,y))
            posicion = (x,y)
            if posicion in pixeles:
                n = (g+b) // 2
                if x > 420 and y > 200:
                    pixeles_falla.add(posicion)
                nueva_imagen.putpixel(posicion, (n,g,b))
            else:
                nueva_imagen.putpixel((x,y), (r,g,b))

    return nueva_imagen, pixeles_falla

def pasada3(imagen: Image, pixeles):

    factor = 32

    ancho, alto = imagen.size

    nueva_imagen = Image.new('RGB', (ancho,alto))

    randoms = [
        (168,171,160),
        (192,194,189),
        (159,159,151),
        (223,224,216),
        (72,63,65),
    ]

    for x in range(ancho):
        for y in range(alto):
            r,g,b = imagen.getpixel((x,y))            
            if (x,y) in pixeles and is_grande(r,g,factor) and is_grande(r,b,factor):
                p = promedio(r,g,b)
                if p < 180 and p > 10:                  
                    valor_random = random.choice(randoms)
                    r1,g1,b1 = valor_random
                    r1 = r1 - random.randint(-8, 8) if random.random() > 0.5 else r1
                    g1 = g1 - random.randint(-8, 8) if random.random() > 0.5 else g1
                    b1 = b1 - random.randint(-8, 8) if random.random() > 0.5 else b1
                    nueva_imagen.putpixel((x,y),(r1,g1,b1))
                else:
                    nueva_imagen.putpixel((x,y), (r,g,b))
            else:
                nueva_imagen.putpixel((x,y), (r,g,b))

    return nueva_imagen

def pasada4(imagen: Image, pixeles):

    factor = 32

    ancho, alto = imagen.size

    nueva_imagen = Image.new('RGB', (ancho,alto))

    randoms = [
        (168,171,160),
        (192,194,189),
        (159,159,151),
        (223,224,216),
        (72,63,65),
        (163, 163, 163),
        (160, 160, 160),
        (152, 152, 152),
        (182, 182, 182),
        (175, 175, 175),
        (173, 173, 173),
        (173, 173, 173),
        (164, 164, 164),
        (173, 173, 173),
        (163, 163, 163)
    ]

    for x in range(ancho):
        for y in range(alto):
            r,g,b = imagen.getpixel((x,y))            
            if (x,y) in pixeles and x < 400 and y > 150:                    
                    valor_random = random.choice(randoms)
                    r1,g1,b1 = valor_random
                    # r1 = r1 - random.randint(-8, 8) if random.random() > 0.5 else r1
                    # g1 = g1 - random.randint(-8, 8) if random.random() > 0.5 else g1
                    # b1 = b1 - random.randint(-8, 8) if random.random() > 0.5 else b1
                    nueva_imagen.putpixel((x,y),valor_random)
            else:
                nueva_imagen.putpixel((x,y), (r,g,b))

    return nueva_imagen


def remove_1():
    imagen = Image.open('./imgs/einvigi_10_halldor_1.jpg')
    imagen.convert('RGB')
    imagen_pasada1, pmc, pcab, pncab = pasada1(imagen)
    imagen_pasada2, pf = pasada2(imagen_pasada1, pncab)
    imagen_pasada2.show()

def remove_6():
    imagen = Image.open('./imgs/einvigi_10_halldor_6.jpg')
    imagen.convert('RGB')
    imagen_pasada1, pmc, pcab, pncab = pasada1(imagen)    
    imagen_pasada2, pf = pasada2(imagen_pasada1, pncab)
    imagen_pasada2.show()

def remove_8():
    imagen = Image.open('./imgs/einvigi_10_halldor_8.jpg')
    imagen.convert('RGB')
    imagen_pasada1, pmc, pcab, pncab = pasada1(imagen)    
    imagen_pasada2, pf = pasada2(imagen_pasada1, pncab)
    imagen_pasada3 = pasada3(imagen_pasada2,pncab)
    imagen_pasada4 = pasada4(imagen_pasada3,pncab)
    imagen_pasada4.show()

remove_1()
remove_6()
remove_8()
