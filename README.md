# Guia1noSQL
# Instrucciones para el manejo de CRUD (Windows)

## Instalacion de dependencias

### Dataset

1.- importar el dataset encontrado en la carpeta Dataset dentro de MongoDBCompass

2.- para esto le damos a **"Create Database"**, le llamamos **"Database"** y a la colección le llamamos **"vct"** y creamos la base de datos

3.- Una vez creada importamos el dataset en **"Add Data"**

### Creacion de entorno Virtual
1.- Instalacion virtual env con

```bash
pip install virtualenv
```

2.- Creacion del ambiente virtual utilizando virtualenv

3.- Crear la carpeta para el ambiente con el comando

```bash
python -m venv "NombreCarpeta"
```

4.- Dirigirse a la carpeta de scripts creada y utiliza

```bash
.\activate
```

5.- Una vez dentro instalar pymongo y los archivos dentro de **"Requirements.txt"** dentro de 
la carpeta CRUD

```bash
pip install pymongo
```

6.- Dentro de esta misma carpeta inicializamos el programa con

```bash
Python CrudGuia1.py
```

## Esquema de la BDD
La base de datos esta compuesta por 2 parametros

1) Player, que indica el nombre de los jugadores que participaron, representada por un string
2) "Player ID", que indica la ID de los jugadores para reconocerlos en el torneo, representada por un int
