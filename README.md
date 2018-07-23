## Documentacion del proyecto

Caracteristicas tecnicas del proyecto:

* Python 3
* Base de datos postgres

El siguiente proyecto, fue implementado con las siguietnes herramientas:

* Falcon: Nos proporciona la creacion de las apis res
* SqlAlchemy : Un Orm que nos permite crear y mapear nuesta basde de datos y tener un mejro control de ella

Al analizar el desarrollo se llego a al siguiente mapeo de las tablas:

![](/img/diagrama.png)

Instalación del proyecto:

En el proyecto podremos encontrar un archivo llamado **requiremets.txt **donde trae todas las dependencias correspondientes para el correcto funcionamiento del proyecto.

Para instalar las dependencias ejecutar el siguiente comando:

```
pip install -r requirements.txt
```

Una vez que el proyecto haya instalado las dependencias, ejecutar el siguietne comando, que nos permitira levantar el servidor y empezar a consumir las apis

```
gunicorn main:app --reload
```

Observaciones:

En caso de que estes utilizando linux o mac, debes dar permisos de escritura o lectura y ejecutarlo en modo superusuario

