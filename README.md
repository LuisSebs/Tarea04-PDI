# Tarea04: Marca de agua

## Autor: Arrieta Mancera Luis Sebastian (318174116)

<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnZwajZkM3A2Z2VmdThqdGpwMGF1ODFrd3Jyd3ZmOTlpbGpwanFzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3kNlg9EzLth22d8XdC/giphy-downsized-large.gif" width="400px"/>

La marca de agua funciona como un fundido en la imagen, utiliza una técnica de mezclado controlado por un factor. Pero no solo se puede usar para poner la molesta marca de agua, sino también para poder crear imagenes bonitas como las que podras visualizar en esta tarea.

# Dependencias

+ [Colorama](https://pypi.org/project/colorama/): `pip install colorama`
+ [Pillow](https://pypi.org/project/pillow/): `pip install pillow`
+ [Argparse](https://pypi.org/project/argparse/): `pip install argparse`

# Ejecución

Favor de instalar las dependencias necesarias. Ejecuta con **python** o **python3** el archivo `main.py`. Te recomiendo usar las imagenes que se encuentran en la carpeta `imgs/`, pero si gustas puedes probar con tus propias imagenes. Al momento de ejcutar el programa deberas ingresar la **ruta de la imagen1**, la **ruta de la imagen 2** y la **ruta de salida de la imagen mezclada**. Puedes configurar más parámetros, te recomiendo los revises con el comando `python3 main.py --help`, este comando enlistará los parámetros que recibe el programa, además de una pequeña descripción del mismo. A continuación se enlistan los parametros que recibe el programa:

**Argumentos obligatorios:**

+ Ruta de la primer imagen
+ Ruta de la segunda imagen
+ Ruta de la salida de la imagen

**Argumentos opcionales**

+ `--s`: Indica si se quiere mostrar la imagen al finalizar.
+ `--f` \<Valor\>: Establece el factor de mezcla de las imagenes (de la primer imagen a la segunda). Este tiene que ser un valor entre `0.0` y `1.0`, el valor por defecto es `0.5`.

# Ejemplos

Te recomiendo pruebes con los siguientes ejemplos, estoy seguro que te gustaran:

```bash
python3 main.py ./imgs/tree1.jpg ./imgs/moon1.jpg ./blending1.jpg --s --f 0.5
```

```bash
python3 main.py ./imgs/birds.jpg ./imgs/moon2.jpg ./blending2.jpg --s --f 0.5
```

```bash
python3 main.py ./imgs/galaxy.jpg ./imgs/tree2.jpg ./blending3.jpg --s --f 0.5
```






