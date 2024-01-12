import funciones.corefile as cf
formatos = {}
cf.MY_DATABASE = "data/formatos.json"
def Newformato(formato:dict):
    formatos.update(formato)
    cf.AddData(formato["id"])

def delformato():
    id = input("Ingrese el id de la formato: ")
    cf.Eliminar(id,formatos)

def modifyformato(llave:str, formato:dict):
    formatos[llave].update(formato)
    cf.NewFile(formatos)

def searchformato()->dict:
    id = input("ingrese el id de la formato: ")
    return formatos.get(id,{})

def validarArchivoformatos():
    if cf.checkFile():
        print("ok")
    else:
        cf.NewFile(formatos)
