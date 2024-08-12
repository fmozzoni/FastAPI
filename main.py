from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


#Asigno el nombre a mi aplicación
app = FastAPI()

movies = [
    {"id":1,"titulo":"La momia", "genero": "Acción", "duracion": "2:05"},
    {"id":2,"titulo":"Camila", "genero": "Romantica", "duracion": "2:23"},
    {"id":3,"titulo":"Gladiador", "genero": "Acción", "duracion": "3:01"},
    {"id":4,"titulo":"Caballos Salvajes", "genero": "Acción", "duracion": "2:34"},
    {"id":5,"titulo":"48 hs", "genero": "Policial", "duracion": "2:15"},
    {"id":6,"titulo":"Mi madre", "genero": "Drama", "duracion": "2:33"},
    {"id":6,"titulo":"Titanic", "genero": "Romantica", "duracion": "3:13"}
]

#Creo una ruta basica al home de mi aplicación
@app.get('/', tags=['Home'])

# Creo una funcion simple que devuelve un texto
def home():
    return "hola mundo"

#Creo otro endpoint en mi aplicación
@app.get('/Movies', tags=['Movies'])

# Creo una funcion simple que devuelve un texto
def home():
    return HTMLResponse('<h1>Hola Mundo<h1>')

#Creo otro endpoint con parámetros en mi aplicación
@app.get('/Movies/{id}', tags=['Movies'])
def getMovie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return []
    
@app.post('/Movies', tags=['Movies'])
def createMovie(pid: int, ptitulo: str, pgenero: str, pduracion: str):
    movies.append({"id": pid, "titulo": ptitulo, "genero": pgenero, "duracion": pduracion})
    return movies

@app.post('/Movies', tags=['Movies'])
def createMovie1(pid: int = Body(), ptitulo: str = Body(), pgenero: str = Body(), pduracion: str = Body()):
    movies.append({"id": pid, "titulo": ptitulo, "genero": pgenero, "duracion": pduracion})
    return movies
