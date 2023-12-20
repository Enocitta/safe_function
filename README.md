

<p style='font-size:160%; text-align:center'><img  src="doc/SF-escudo.jpg" alt="Safe Function" width="100px"/></p>
<div style='font-size:160%; text-align:center;text-decoration: overline; vertical-align:baseline; font-family:courier;'>Safe Function</div>


## Decorador de funciones para debug de Errores de Tipo, en llamadas de tiempo de ejecucion.

El siguiente es un simple desarrollo para controlar que las variables que se ingresan en las funciones corresponden con las especificaciones declaradas en el prototipo de la funcion, en caso de no ser asi evita la ejecucuin de la funcion decorada y realiza el trasado de errores por log



**Table of Contents**  

  - [Titulo](#decorador-de-funciones-para-debug-de-errores-de-tipo-en-llamadas-de-tiempo-de-ejecucion)
  - [Ejemplo](#ejemplo)
  - [Instalación](#instalaci%C3%B3n)
  - [Tests](#tests)
  - [Convenciones de estilo](#convenciones-de-estilo)
  - [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Ejemplo

En esta sección se muestra cómo usar el paquete con un ejemplo sencillo.

```python
import safe_function as Sf

@Sf
def funcInt(A: int, B: int ) -> int:
  return A+B

funcInt(1,3) --> "OK ,silent log pass ,the function runs normally"
funcInt(1,"error") --> "the decorator checks for the type error and stops execution"

```
El decorador se puede agregar a una funcion que necesite inspeccionar , evitando su ejecucion si es que no cumple con
los requisitos de invocacion, en caso de utilizarlo en objeto que no sea funcion enviara un `python TypeError`
```python
import safe_function as Sf

@Sf
class myclass:
    pass

ins1 = myclass --> "TypeError"
```

## Instalación

En esta sección se listan los pasos necesarios para instalar el paquete.

- Instalar Python 3 como minimo (se recomienda instalar la version mas reciente)



## Tests
Recuerde que las pruebas dependen de el modulo `nose`
si no lo posee instalelo con 

`pip install nose`

En la libreria se encuentra el archivo `test_safe_function.py` el cual contiene las pruebas de ejecucuion
en la terminal de `PyCharm` por ejemplo puede correr
- `nosetests` (corre todos los tests)
```...........
----------------------------------------------------------------------
Ran 11 tests in 0.003s

OK
```
 
## Convenciones de estilo

Este proyecto sigue las convenciones de la [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Ver un ejemplo completo del [uso de docstrings en python según la guía de Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)

## License
[GPL](https://www.gnu.org/licenses/gpl-3.0.html)
