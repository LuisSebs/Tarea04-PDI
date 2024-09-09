import argparse
from PIL import Image
from utils.progress_bar import progress_bar
from utils.colores import random_color, rojo, verde, azul, reset

def blending(imagen1: Image, imagen2: Image, mix=0.5):
    """
        Recibe dos imagenes y las mezcla

        Parameters :
        ------------

            imagen1:
                imagen de pillow
            
            imagen2:
                imagen de pillow

            mix:
                factor de mezclado (de la imagen1 a la imagen2)

        Returns :
        ---------

            imagen resultante de la mezcla de las dos imagenes
    """

    # Verificamos si alguna de las imágenes tiene transparencia (canal alfa)
    modo_imagen1 = 'RGBA' if imagen1.mode == 'RGBA' else 'RGB'
    modo_imagen2 = 'RGBA' if imagen2.mode == 'RGBA' else 'RGB'

    # Convertimos ambas imágenes al mismo modo para evitar problemas de mezcla
    imagen1 = imagen1.convert(modo_imagen1)
    imagen2 = imagen2.convert(modo_imagen2)

    # Imagen pequeña
    imagen_menor = None
    # Imagen grande
    imagen_mayor = None

    # Determinamos cuál imagen es más pequeña
    if imagen1.size >= imagen2.size:
        imagen_menor = imagen2
        imagen_mayor = imagen1.resize(imagen2.size)
    else:
        imagen_menor = imagen1
        imagen_mayor = imagen2.resize(imagen1.size)

    # Alto y ancho de la nueva imagen
    ancho, alto = imagen_menor.size

    # Nueva imagen
    nueva_imagen = Image.new(imagen_menor.mode,(ancho,alto))

    # Barra de progreso
    total_pixeles = ancho * alto
    pixeles_procesados = 0
    porcentaje_progreso = 0 
    color = random_color()

    print(random_color()+'Generando blending'+reset)

    # Mezclamos las dos imagenes
    for x in range (ancho):
        for y in range(alto):
            # canales del pixel de la imagen 1
            r1, g1, b1 = imagen_menor.getpixel((x,y))
            # canales del pixel de la imagen 2
            r2, g2, b2 = imagen_mayor.getpixel((x,y))
            
            # Canales del nuevo pixel
            rn = int((r1 * mix) + (r2 * (1.0 - mix)))
            gn = int((g1 * mix) + (g2 * (1.0 - mix)))
            bn = int((b1 * mix) + (b2 * (1.0 - mix)))

            # Añadimos el nuevo pixel a la imagen
            nueva_imagen.putpixel((x,y), (rn,gn,bn))

            # Actualizamos la barra de progreso
            pixeles_procesados += 1

            # Actualizamos el porcentaje de progreso
            nuevo_porcentaje_progreso = (pixeles_procesados * 100) // total_pixeles

            # Mostramos el progreso cada 10%
            if nuevo_porcentaje_progreso >= porcentaje_progreso + 10:
                porcentaje_progreso = nuevo_porcentaje_progreso
                progress_bar(pixeles_procesados, total_pixeles, color)
                color = random_color()

    print(random_color()+"Blending terminado ʕ•ᴥ•ʔ"+reset)
                
    return nueva_imagen

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa que mezcla dos imagenes")

    # Argumentos no opcionales
    parser.add_argument("ruta_imagen1", help="Ruta de la primer imagen")
    parser.add_argument("ruta_imagen2", help="Ruta de la segunda imagen")
    parser.add_argument("ruta_salida", default=None, help="Ruta de la salida de la imagen")

    # Argumentos opcionales
    parser.add_argument("--s", action="store_true", help="Indica si se quiere mostrar la imagen al terminar")
    parser.add_argument("--f", default=0.5, help="Factor de mezcla de las imagenes (de la primer imagen a la segunda). el valor debe estar entre 0.0 y 1.0")

    # Obtenemos los argumentos
    args = parser.parse_args()

    # Cargamos las imagenes
    imagen1 = None
    imagen2 = None
    try:
        imagen1 = Image.open(args.ruta_imagen1)
        imagen2 = Image.open(args.ruta_imagen2)
    except Exception as e:
        print(rojo+f"Error al cargas las imagenes: {e}"+reset)

    # Mezclamos las imagenes
    blend = blending(
        imagen1=imagen1,
        imagen2=imagen2,
        mix=float(args.f)
    )
    # Guardamos la imagen
    blend.save(args.ruta_salida)
        
    if args.s:
        # Mostramos la imagen
        blend.show()

# imagen1 = Image.open('./imgs/tree1.jpg')
# imagen2 = Image.open('./imgs/moon1.jpg')

# imagen1 = Image.open('./imgs/birds.jpg')
# imagen2 = Image.open('./imgs/moon2.jpg')

# imagen1 = Image.open('./imgs/galaxy.jpg')
# imagen2 = Image.open('./imgs/tree2.jpg')

# marca_de_agua(imagen1,imagen2).show()


    