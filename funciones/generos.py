import funciones.corefile as cf
generos = {}
cf.MY_DATABASE = "data/generos.json"
def Newgenero(genero:dict):
    generos.update(genero)
    cf.AddData(genero["id", generos])

def delgenero():
    id = input("Ingrese el id de la genero: ")
    cf.Eliminar(id,generos)

def modifygenero(llave:str, genero:dict):
    generos[llave].update(genero)
    cf.NewFile(generos)

def searchgenero()->dict:
    id = input("ingrese el id de la genero: ")
    return generos.get(id,{})

def validarArchivogeneros():
    if cf.checkFile():
        print("ok")
    else:
        cf.NewFile(generos)
