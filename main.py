import os
import ui.mainMenu as menu
sistemaMenu = "[1] -> Administrador de Generos\
    \n[2] -> Administrador de Actores\
    \n[3] -> Administrador de Formatos\
    \n[4] -> Gestor de Peliculas\
    \n[5] -> Gestor de informes\
    \n[6] -> Salir\
    \nSeleccion: "
def main ():
    header = """
    *********************************************
    *  SISTEMA GESTOR DE PELICULAS BLOCKBUSTER  *
    *********************************************
    """
    while True:
        print(header)
        op = input(sistemaMenu)
        match op:
            case "1":
                os.system("cls")
                menu.GestorGeneros()
                os.system("pause")
                os.system("cls")
            case "2":
                os.system("cls")
                menu.GestorActores()
                os.system("pause")
                os.system("cls")
            case "3":
                os.system("cls")
                menu.GestorFormatos()
                os.system("pause")
                os.system("cls")
            case "4":
                os.system("cls")
                menu.GestorPeliculas()
                os.system("pause")
                os.system("cls")
            case "5":
                os.system("cls")
                menu.GestorInformes()
                os.system("pause")
                os.system("cls")
            case "6":
                break
            case _:
                print("[¡] Ingrese una opción válida")
                os.system("pause")
                os.system("cls")



if __name__ == "__main__":
    main()