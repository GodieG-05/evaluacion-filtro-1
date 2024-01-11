import funciones.corefile as cf
peliculas = {}
cf.MY_DATABASE = "data/peliculas.json"
def NewPelicula(pelicula:dict):
    peliculas.update(pelicula)
    cf.AddData(pelicula["id", peliculas])

def delPelicula():
    id = input("Ingrese el id de la pelicula: ")
    cf.Eliminar(id,peliculas)

def modifyPelicula(llave:str, pelicula:dict):
    peliculas[llave].update(pelicula)
    cf.NewFile(peliculas)

def searchPelicula()->dict:
    id = input("ingrese el id de la pelicula: ")
    return peliculas.get(id,{})

def validarArchivoPeliculas():
    if cf.checkFile():
        print("ok")
    else:
        cf.NewFile(peliculas)
