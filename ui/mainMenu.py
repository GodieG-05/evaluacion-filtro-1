import os
import funciones.corefile as cf
import funciones.peliculas as p
import funciones.generos as g
import funciones.actores as a
import funciones.formatos as f
import funciones.informes as i

def GestorGeneros():
    generosMenu = "[1] -> Crear genero\
    \n[2] -> Listar generos\
    \n[3] -> Ir Menu principal\
    \nSeleccion: "
    header1 = """
    *****************************
    *     GESTOR DE GENEROS     *
    *****************************
        """
    while True:
        print(header1)

        op = input(generosMenu)

        match op:
            case "1":
                generos = {
                    "generos":{
                            "G01":{
                                "id":"G01",
                                "nombre":input("ingrese el nombre del genero de la pelicula: ")
                            }
                        }
                    }
                g.Newgenero(generos)      
            case "2":
                for clave, valor in generos.items():
                    print(f"{clave}: {valor}")
            case "3":
                break
            case _:
                print("[¡] Ingrese una opción válida")
                os.system("pause")
                os.system("cls")
    
def GestorActores():
    actoresMenu = "[1] -> Crear Actor\
    \n[2] -> Listar Actor\
    \n[3] -> Ir Menu principal\
    \nSeleccion: "
    header = """
    *****************************
    *     GESTOR DE ACTORES     *
    *****************************
    """
    while True:
        print(header)

        op = input(actoresMenu)

        match op:
            case "1":
                actores={
                        "actores":{
                            "A01":{
                                "id":"A01",
                                "nombre":input("ingrese el nombre del actor de la pelicula: "),
                                "rol":input("ingrese el rol del actor de la pelicula. protagonista/antagonista/reparto: ")
                            }
                        }
                    }
                a.Newactor(actores)
            case "2":
                for clave, valor in actores.items():
                    print(f"{clave}: {valor}")
            case "3":
                break
            case _:
                print("[¡] Ingrese una opción válida")


def GestorFormatos():
    formatosMenu = "[1] -> Crear formatos\
    \n[2] -> Listar formatos\
    \n[3] -> Ir Menu principal\
    \nSeleccion: "
    header = """
    *****************************
    *     GESTOR DE FORMATOS    *
    *****************************
    """
    while True:
        print(header)

        op = input(formatosMenu)

        match op:
            case "1":
                formatos ={
                    "formato":{
                            "F01":{
                                "id":"F01",
                                "nombre":input("Ingrese el nombre del formato de la pelicula: "),
                                "NroCopias":input("Ingrese el numero de copias: "),           
                                "valorPrestamo":input("Ingrese el valor del prestamo: ")
                            }
                        }
                    }
                f.Newformato(formatos)    
            case "2":
                for clave, valor in formatos.items():
                    print(f"{clave}: {valor}")
            case "3":
                break
            case _:
                print("[¡] Ingrese una opción válida")

def GestorPeliculas():
    peliculasMenu = "[1] -> Agregar pelicula\
    \n[2] -> Editar pelicula\
    \n[3] -> Eliminar pelicula\
    \n[4] -> Eliminar Actor\
    \n[5] -> Buscar pelicula\
    \n[6] -> Listar todas las peliculas\
    \n[7] -> Menu principal\
    \nSeleccion: "
    header = """
    *****************************
    *    GESTOR DE PELICULAS    *
    *****************************
    """
    cf.checkFile(p.peliculas)
    while True:
        print(header)

        op = input(peliculasMenu)

        match op:
            case "1":
        
                pelicula = {
                    
                        "id":"",
                        "nombre":"",
                        "duracion":"",
                        "sinopsis":""
                            
                        }
                
                for clave, valor in pelicula.items():
                    pelicula[clave] = input(f"Ingrese {clave.capitalize()} de la pelicula: ")
        
                generos = {
                            "generos":{
                            "G01":{
                                "id":input("Ingrese el Id del genero de la pelicula: "),
                                "nombre":input("ingrese el nombre del genero de la pelicula: ")
                            }
                        }
                    }
                pelicula.update(generos)
                
                actores = {
                            "actores":{
                            "A01":{
                                "id":input("Ingrese el Id del del actor de la pelicula: "),
                                "nombre":input("ingrese el nombre del actor de la pelicula: "),
                                "rol":input("ingrese el rol del actor de la pelicula. protagonista/antagonista/reparto: ")
                            }
                        }
                    }
                pelicula.update(actores)

                formatos = {
                            "formato":{
                            "F01":{
                                "id":"",
                                "nombre":"",
                                "NroCopias":0,           
                                "valorPrestamo":0
                            }
                        }
                    }
    
                for clave, valor in formatos["formato"].items():
                    if (valor!= "NroCopias" and clave != "valorPrestamos"):
                        formatos[valor] = input(f"Ingrese {clave.capitalize()} de la pelicula: ")
                    else:
                        while True:    
                            try:
                                formatos["NroCopias"] = int(input(f"Ingrese el numero de copias de la pelicula: "))
                            except ValueError:
                                print("Se espera un numero entero")
                            else:
                                break
                        while True:    
                            try:
                                formatos["valorPrestamo"] = int(input(f"Ingrese el valor del prestamo de la pelicula: "))
                            except ValueError:
                                print("Se espera un numero entero")
                            else:
                                break
                pelicula.update(formatos)
                print(pelicula)
                #p.NewPelicula(pelicula)
            case "2":
                p.delPelicula()
            case "3":
                data = p.searchPelicula()
                if (len(data)):
                    p.modifyPelicula(data["id"],data)
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                break
            case _:
                print("[¡] Ingrese una opción válida")

def GestorInformes():
    informesMenu = "[1] -> Listar las peliculas de un genero especifico\
    \n[2] -> Listar las peliculas donde el protagonista sea Silvester Stallone\
    \n[3] -> Buscar pelicula y mostrar la sinopsis y los actores\
    \n[4] -> Ir Menu principal\
    \nSeleccion: "
    header = """
    *****************************
    *     GESTOR DE INFORMES    *
    *****************************
    """
    while True:
        print(header)

        input(informesMenu)

        match informesMenu:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                break
            case _:
                print("[¡] Ingrese una opción válida")


