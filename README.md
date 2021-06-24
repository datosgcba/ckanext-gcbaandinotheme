# [Data.buenosaires.gob.ar](https://data.buenosaires.gob.ar/)

Repositorio de la extensión del Portal [data.buenosaires.gob.ar](http://data.buenosaires.gob.ar/) de la Ciudad de Buenos Aires para [CKAN](http://ckan.org/). Este proyecto se encarga de modificaciones al ruteo de la aplicación web, cambios visuales a la interfaz, y customización del portal, entre otros. Este repositorio *no* constituye el proyecto entero.

- [Instalación](#instalaci%C3%B3n)
- [Estructura de archivos](#estructura-de-archivos)
- [Uso del theme](#uso-del-theme)
- [Créditos](#cr%C3%A9ditos)

## Instalación

Correr dentro del entorno virtual de python(venv) para instalaciones hechas con Docker:

    pip install -e "git+https://github.com/datosgcba/ckanext-gcbaandinotheme.git@ckan2.9_assessment#egg=ckanext-gobar_theme"

### Estructura de archivos

```
- ckanext
    - gobar_theme
        - asset
            - js
                - archivos de js a ser importados por los distintos templates html
            - styles
                - archivos css generados desde sus versiones de scss
        - public
            - assets estáticos y públicos como imagenes y fuentes
        - templates
            - archivos de jinja renderizados por los controladores
        - actions.py # lógica de modelos de ckan, sobreescribe y/o extiende la lógica de ckan
        - controller.py # controladores para la home y la api, sobreescriben y/o extienden la lógica de ckan
        - helpers.py # metodos auxiliares para renderizado de templates
        - package_controller.py # controlador de lógica de datasets y recursos, sobreescribe y/o extiende la lógica de ckan
        - plugin.py # archivo que registra el repositorio como extensión de ckan y declara acciones, helpers y ruteo
```

## Uso del theme

La extensión sirve para darle una nueva vista al CKAN original, fue desarrollada utilizando como base el gobar_theme de Nación(https://github.com/datosgobar/datos.gob.ar) y refactorizado para darle la visual requerida por el Gobierno de la Ciudad de Buenos Aires. Aún contiene algunas fallas en los estilos debido a las nuevas actualizaciones que sufrió el CKAN y que fueron "parcheadas" sobre la marcha.

## Créditos

Este proyecto está basado en [CKAN](https://github.com/ckan/ckan) y en la [guia para crear extensiones](http://docs.ckan.org/en/latest/extensions/tutorial.html).
