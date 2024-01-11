import funciones.corefile as cf
peliculas = {}
cf.MY_DATABASE = "data/peliculas.json"



def searchPelicula()->dict:
    id = input("ingrese el id de la pelicula: ")
    return peliculas.get(id,{})

