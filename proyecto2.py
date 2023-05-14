import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


inicioSesion = True

ventanaDos = True
usuarioActual = ""

def ventana_2():
        ventana = tkinter.Tk()  # es la ventana grafica
        ventana.title("Waze mini")
        ventana.wm_attributes("-fullscreen", True)   # Fullscreen
        print(usuarioActual)
        # Titulo 
        titulo = tkinter.Label(ventana,text = "Waze",font = ("Impact", 25),bd = 0,padx = 0, pady = 0 ,relief = "groove",fg = "gray50") 
        mini = tkinter.Label(ventana,text = "mini",font = ("Verdana", 15,"italic"),bd = 0,padx = 0,pady = 0,relief = "groove",fg = "gray45")
        titulo.place(x=10,y=5)
        mini.place(x = 85,y = 18)
        
        """
        # Crear la barra de menú
        menu = tk.Menu(ventana)
        ventana.config(menu = menu)

        # Crear el elemento del menú
        archivo = tk.Menu(menu)
        menu.add_cascade(label = "Opciones",menu = archivo)
        archivo.add_command(label="Salir",command = lambda: ventana.destroy())
        """
        def cargarMapa():
            print("cargar")

        def seleccionarDestino():
            print("seleccionar")

        def planificarDestino():
            print("planificar")

        def guardarDestino():
            print("guardar")

        def borrarDestino():
            print("borrar")

        def modificarMapa():
            print("modificar")

        def salir():
            salir = messagebox.askyesno(message = "¿Esta seguro?",title = "Salir")
            if salir:
                ventana.destroy()
                
            
        #Botones opciones principales

        # Cargar Mapa
        cargarMapaBoton = tk.Button(ventana, text = "Cargar Mapa",font = ("Verdana", 12)
                                    ,bd = 2, bg = "gray30",relief = "flat",fg = "gray92",padx = 55, pady =2, command = cargarMapa).place(x = 25, y = 70)
        # Seleccionar Destino
        seleccionarDestinoBoton = tk.Button(ventana, text = "Seleccionar Destino",font = ("Verdana", 12)
                                    ,bd = 2, bg = "gray30",relief = "flat",fg = "gray92",padx = 26, pady = 2,command = seleccionarDestino).place(x = 25, y = 115)
        #Planificar Destino
        planificarDestinoBoton = tk.Button(ventana, text = "Planificar Destino",font = ("Verdana", 12)
                                    ,bd = 2, bg = "gray30",relief = "flat",fg = "gray92",padx = 35, pady = 2,command = planificarDestino).place(x = 25, y = 160)
        #Guardar Destino
        guardarDestinoBoton = tk.Button(ventana, text = "Guardar Destino",font = ("Verdana", 12)
                                    ,bd = 2, bg = "gray30",relief = "flat",fg = "gray92",padx = 40, pady = 2,command = guardarDestino).place(x = 25, y = 205)
        #Borrar Destino
        borrarDestinoBoton = tk.Button(ventana, text = "Borrar Destino",font = ("Verdana", 12)
                                    ,bd = 2, bg = "gray30",relief = "flat",fg = "gray92",padx = 48, pady = 2,command = borrarDestino).place(x = 25, y = 250)
        #Modificar Mapa
        modificarMapaBoton = tk.Button(ventana, text = "Modificar Mapa",font = ("Verdana", 12)
                                    ,bd = 2, bg = "gray30",relief = "flat",fg = "gray92",padx = 46, pady = 2,command = modificarMapa).place(x = 25, y = 295)
        #Salir
        salirBoton = tk.Button(ventana, text = "Salir",font = ("Verdana", 12)
                                    ,bd = 2, bg = "gray30",relief = "flat",fg = "gray92",padx = 90, pady = 2,command = salir).place(x = 25, y = 340)




       
        ventana.mainloop()

def ventana_1():
    
    # Ventana inicial
    ventana = tkinter.Tk()  # es la ventana grafica
    ventana.title("Inicio de sesión")
    ventana.geometry("925x600") # cambia el tamano de la ventana
    ventana.resizable(False,False) # no permite maxmizar la pantalla
    color = tkinter.Label(ventana,bg = "gray60")      # Color Fondo
    color.pack(fill = tkinter.BOTH,expand = True)
     
    # Titulo 
    titulo = tkinter.Label(ventana,text = "Waze",font = ("Impact", 35),bd = 0, bg = "gray60",padx = 0, pady = 0 ,relief = "groove",fg = "white") 
    mini = tkinter.Label(ventana,text = "mini",font = ("Verdana", 15,"italic"),bd = 0, bg = "gray60",padx = 0,pady = 0,relief = "groove",fg = "white")
    mini.place(x = 470, y = 48)
    titulo.place(x= 365, y = 20)
    """
    img = tk.PhotoImage(file = "logo.png")
    etiquetaImagen = tk.Label(ventana, image = img, bg = "gray60")
    etiquetaImagen.place(x = 500,y = 20)
    """
    # Iniciar Sesion 
    etiquetaInicio = tkinter.Label(ventana,text = "Iniciar Sesión" ,font = ("Verdana", 25,"italic"),bd = 0, bg = "gray60",relief = "groove",fg = "gray95",padx = 0, pady = 0)  
    etiquetaInicio.place(x= 100, y= 125)

    # Etiqueta de usurario
    etiquetaUsuario = tkinter.Label(ventana,text = "~~~~Ingrese su usuario~~~~~" ,font = ("Verdana", 14,"italic"),bd = 0, bg = "gray60",relief = "groove",fg = "gray92",padx = 0, pady = 0)  
    etiquetaUsuario.place(x= 45, y= 195)

    # Entrada de usuario
    ingresarUsuario = tkinter.Entry(ventana, font = ("Verdana", 12),width = 20, bd = 0, bg = "gray90",relief = "groove", fg = "gray40")
    ingresarUsuario.place(x= 100, y= 245)

    #Etiqueta contrasena
    etiquetaContrasena = tkinter.Label(ventana,text = "~~~Ingrese su contraseña~~~~" ,font = ("Verdana", 14,"italic"),bd = 0, bg = "gray60",relief = "groove",fg = "gray92",padx = 0, pady = 0)  
    etiquetaContrasena.place(x= 45, y= 300)

    # Entrada contrasena
    ingresarContrasena = tkinter.Entry(ventana, font = ("Verdana", 12),width = 20, bd = 0, bg = "gray90",relief = "groove", fg = "gray40", show = "*")
    ingresarContrasena.place(x= 100, y= 360)

    def verificar():
        # Obtiene los valores ingresado de usuario y contrasena
        
        global usuarioActual
        usuario_A_verificar = ingresarUsuario.get()
        usuarioActual = usuario_A_verificar         # guarda el usuario en la variable global
        contrasena_A_verificar = ingresarContrasena.get()

        if usuario_A_verificar == "" and contrasena_A_verificar == "":
            messagebox.showerror(message = "Porfavor ingrese su usuario y contraseña", title = "Error")
        else:
            archivo = open("Usuario.txt", encoding="utf-8", mode="r")
            lineas = archivo.readlines()
            archivo.close()
            coincidencia = False
            
            for linea in lineas:  
                contenido = linea.strip().split(";")
                usuario = contenido[0]
                contrasena = contenido[1]
                if usuario_A_verificar == usuario and contrasena_A_verificar == contrasena:
                    coincidencia = True
                else:
                    continue
            if coincidencia == True :
                ventana.destroy()
                return ventana_2()
            else:
                messagebox.showerror(message = "Error usuario o contraseña incorrectos", title = "Error")
          

    # Boton iniciar sesion 
    iniciarSesionB = tk.Button(ventana, text = "Iniciar Sesión",font = ("Verdana", 15,"italic"),bd = 2, bg = "gray25",relief = "sunken",fg = "gray92",padx = 80, pady = 3, command = verificar)
    iniciarSesionB.place(x = 60, y = 450)
    


    ventana.mainloop()



if inicioSesion:
    ventana_1()

if ventanaDos:
    ventana_2()
    



