
Safe Function
===

[![python.py]](https://github.com/Enocitta/safe_function?branch=master)
[![Build Status](https://travis-ci.org/abenassi/Project-Example-1.svg)](https://travis-ci.org/abenassi/Project-Example-1)
Decorador de funciones para debug de Errores de Tipo, en llamadas de tiempo de ejecucion

El siguiente es un simple desarrollo para controlar que las variables que se ingresan en las funciones corresponden con las especificaciones declaradas en el prototipo de la funcion, en caso de no ser asi evita la ejecucuin de la funcion decorada y realiza el trasado de errores por log


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [One liner que dice qué es el proyecto](#one-liner-que-dice-qu%C3%A9-es-el-proyecto)
  - [Ejemplo](#ejemplo)
  - [Instalación](#instalaci%C3%B3n)
  - [Tests](#tests)
  - [Convenciones de estilo](#convenciones-de-estilo)

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

## Instalación

En esta sección se listan los pasos necesarios para instalar el paquete.

- Instalar Python 2.7 (se recomienda instalar [Anaconda](https://www.continuum.io/downloads))
- `brew install dependencia_para_mac` (instala primero cualquier dependencia necesaria)
- `conda create -n my_environment python=2` (crea un entorno virtual -copia limpia de python- donde instalar el proyecto con Anaconda)
- `source activate my_environment` (activa el entorno virtual)
- `pip install -e .` (instala el proyecto en modo edición: los packages listados en el *setup.py* se instalan en el path del entorno virtual de manera que permiten importaciones absolutas)
- `deactivate` (desactiva el entorno virtual)

Alternativamente, si no se utiliza Anaconda se puede usar *virtualenv* para crear entornos virtuales:

- `cd my_project`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -e .`
- `deactivate`

## Tests

En esta sección se muestra como correr los tests.

- `nosetests` (corre todos los tests)

## Convenciones de estilo

Este proyecto sigue las convenciones de la [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Ver un ejemplo completo del [uso de docstrings en python según la guía de Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)

## License
[GPL](https://www.gnu.org/licenses/gpl-3.0.html)
