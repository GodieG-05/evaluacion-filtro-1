import json
import os

MY_DATABASE = ""

def NewFile(*param):
    with open(MY_DATABASE,"w") as nf:
        json.dump(param[0],nf,indent=4)

def AddData(*param):
    with open(MY_DATABASE,"r+") as ad:
        data = json.load(ad)
        
        if (len(param) > 1):
            data.update({param[0]:param[1]})
        else:
            data.update({param[0]})
        
        data.seek(0)
        json.dump(data,ad,indent=4)
        ad.close()

def Eliminar(*param):
    data = list(param)
    data[1].pop(data[0])
    NewFile(data[1])

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)
    
def checkFile(*param):
    data = list(param)
    if (os.path.isfile(MY_DATABASE)):
        if (len(param)):
            data[0].update(ReadFile())
        else:
            if (len(param)):
                NewFile(data[0])