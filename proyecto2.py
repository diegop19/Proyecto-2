import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


inicioSesion = True



def ventana_2():
    print("estas en ventana 2")

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
    mini = tkinter.Label(ventana,text = "mini",font = ("Verdana", 15),bd = 0, bg = "gray60",padx = 0,pady = 0,relief = "groove",fg = "white")
    mini.place(x = 470, y = 48)
    titulo.place(x= 365, y = 20)
    """
    img = tk.PhotoImage(file = "logo.png")
    etiquetaImagen = tk.Label(ventana, image = img, bg = "gray60")
    etiquetaImagen.place(x = 500,y = 20)
    """
    # Iniciar Sesion 
    etiquetaInicio = tkinter.Label(ventana,text = "Iniciar Sesión" ,font = ("Verdana", 25,"italic"),bd = 0, bg = "gray60",relief = "groove",fg = "gray92",padx = 0, pady = 0)  
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
        
        usuario_A_verificar = ingresarUsuario.get()
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





