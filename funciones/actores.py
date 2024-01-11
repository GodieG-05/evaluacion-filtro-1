import funciones.corefile as cf
actores = {}
cf.MY_DATABASE = "data/actores.json"
def Newactor(actor:dict):
    actores.update(actor)
    cf.AddData(actor["id", actores])

def delactor():
    id = input("Ingrese el id de la actor: ")
    cf.Eliminar(id,actores)

def modifyactor(llave:str, actor:dict):
    actores[llave].update(actor)
    cf.NewFile(actores)

def searchactor()->dict:
    id = input("ingrese el id de la actor: ")
    return actores.get(id,{})

def validarArchivoactores():
    if cf.checkFile():
        print("ok")
    else:
        cf.NewFile(actores)
