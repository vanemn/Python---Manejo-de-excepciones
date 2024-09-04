### Photo Gallery Application

## Descripción

Esta aplicación de galería de fotos permite a los usuarios gestionar sus fotos. Se ha implementado un control para asegurar que no se puedan modificar las dimensiones de una foto (alto o ancho) a valores menores a 1 o mayores al valor máximo permitido por la clase Foto. Este control se realiza mediante una excepción personalizada llamada DimensionError.

## error.py
error.py se trabaja con las siguientes consideraciones
- contiene la excepción DimensionError derivada de Exception.
- Se sobreescribe el constructor para recibir los parámetros mensaje, dimension y maximo, y asignarles los respectivos atributos de instancia.
- Sobrecargar el método __str__ para retornar un mensaje adecuado basado en los atributos proporcionados.
## foto.py
En el archivo foto.py, se solicita modificar los métodos setter de alto y ancho para lanzar una excepción DimensionError si el nuevo valor no cumple con las condiciones especificadas.

## Prerrequisitos o Dependencias

Sistema Operativo Windows, Linux, MacOS
Lenguaje de programación Python 3.12

## Instalación del Proyecto

Clonar el repositorio:

```bash
# git@github.com:vanemn/desafio_modulo4_clase10.git
```

Ingresar a la carpeta del proyecto:

```bash
# desafio_modulo4_clase10
```

Autor

- [Vanessa Morales](https://github.com/vanemn)
- [Benjamín Pardo](https://github.com/bpardo02)
- [Nicole Pinilla](https://github.com/Npinilla19)
