from tkinter import *

class Usuario:
  def __init__(self, nombre, edad, sexo, sueldo, AFP):
    self.nombre = nombre 
    self.edad = edad 
    self.sexo = sexo  
    self.sueldo=sueldo 
    self.AFP = AFP 
    
  def Obtenercapital (self):   #Cálculo de la Capital, Con la comisión base del 10% mas la respectiva de cada AFP, además de la rentabilidad de 5%
    if (self.AFP=="Capital" or self.AFP=="capital"):
      capital=self.sueldo*0.1144*1.0453
      return (capital)
    if (self.AFP=="Cuprum" or self.AFP=="cuprum"):
      capital=self.sueldo*0.1144*1.0427
      return (capital)
    if (self.AFP == "Habitat" or self.AFP == "habitat"):
      capital=self.sueldo*0.1127*1.0447
      return (capital)
    if (self.AFP == "Modelo" or self.AFP == "modelo"):
      capital=self.sueldo*0.1077*1.0352
      return (capital)
    if (self.AFP == "Planvital" or self.AFP == "planvital"):
      capital=self.sueldo*0.1116*1.0431
      return (capital)
    if (self.AFP == "Provida" or self.AFP == "provida"):
      capital=self.sueldo*0.1145*1.0452
      return (capital)
    print ("AFP invalida")
     
  def ObtenerPension(self): #Obtencion de la pension, con la esperanza de vida del y la jubilacion de cada sexo respectivamente. (Opcion 1)
     C=self.Obtenercapital()
     if (self.sexo=="Hombre" or self.sexo=="hombre"):
         V1=C*(65-self.edad)
         V2= V1/((79-65))
         return (V2)
     if (self.sexo=="Mujer" or self.sexo=="mujer"):
         V1=C*(60-self.edad)
         V2=V1/((83-60))
         return (V2)

  def VerificarPension(self,estimado): #obtencion del monto restante necesario para llegar al monto objetivo. (Opcion 2)
    pension=self.ObtenerPension()
    dif=estimado-pension
    if dif<0:
      return("La jubilación es mayor que la proyección: " + str(pension))
    if self.sexo == "Hombre":
      N1=dif*20
      N2=(N1/(65-self.edad))
    if self.sexo == "Mujer":
      N1=dif*30
      N2=(N1/(60-self.edad))
    N3=N2*0.97 #Rentabilidad del 3% APV
    return (self.nombre + " debe añadir " + str(N3) + " pesos como APV.")

b=Usuario("Juan",20,"Hombre",10000000,"Capital")
b.VerificarPension(300000)

def principal():
  global main
  main = Tk()
  main.resizable(width=False, height=False)
  main.title("Retirement Simulator")

  main.geometry('500x240')  

  main.configure(background = 'Skyblue')

  info = Label(main, text = "Seleccione la opción que desea:", font = ('Arial Bond', 12))
  info.place(x = 0, y = 0)
  info.configure(background = "Skyblue")
  info1 = Label(main, text = "-Opción 1: Calcular pensión mensual en su respectiva AFP.", font = ('Arial Bond', 12))
  info1.place(x = 0, y = 30)
  info1.configure(background = "Skyblue")
  info2 = Label(main, text = "-Opción 2: Verificar pensión mensual deseada en su respectiva AFP.", font = ('Arial Bond', 12))
  info2.place(x = 0, y = 60)
  info2.configure(background = "Skyblue")
  button1 = Button(main, text = "Opción 1", font = ('Arial Bond', 12))
  button2 = Button(main, text = "Opción 2", font = ('Arial Bond', 12))
  button1.bind("<Button-1>", Opcion1)
  button1.place(x = 100, y = 90)
  button2.bind("<Button-1>", Opcion2)
  button2.place(x = 100, y = 130)

  boton1 = Button(main, text = "Salir", font = ('Arial Bond', 12))
  boton1.bind("<Button-1>", Salir)
  boton1.place(x = 100, y = 170)

  main.mainloop()

def Opcion1(event):
  global ventana
  global texto1
  global texto2
  global texto3
  global texto4
  global texto5
  ventana = Tk()
  ventana.title("Cálculo de pensión")
  main.destroy()
  ventana.configure(background = "Skyblue")

  ventana.geometry("300x250")

  linea1 = Label(ventana, text = "Nombre", font = ("Arial Bond", 15))
  linea1.configure(background = "Skyblue")
  linea2 = Label(ventana, text = "Edad", font = ("Arial Bond", 15))
  linea2.configure(background = "Skyblue")
  linea3 = Label(ventana, text = "Sexo", font = ("Arial Bond", 15))
  linea3.configure(background = "Skyblue")
  linea4 = Label(ventana, text = "Sueldo", font = ("Arial Bond", 15))
  linea4.configure(background = "Skyblue")
  linea5 = Label(ventana, text = "AFP", font = ("Arial Bond", 15))
  linea5.configure(background = "Skyblue")
  texto1 = Entry(ventana)
  texto2 = Entry(ventana)
  texto3 = Entry(ventana)
  texto4 = Entry(ventana)
  texto5 = Entry(ventana)

  linea1.grid(row=0)
  linea2.grid(row=1)
  linea3.grid(row=2)
  linea4.grid(row=3)
  linea5.grid(row=4)

  texto1.grid(row=0, column=1)
  texto2.grid(row=1, column=1)
  texto3.grid(row=2, column=1)
  texto4.grid(row=3, column=1)
  texto5.grid(row=4, column=1)

  boton1 = Button(ventana, text = "Siguiente", command = Siguiente, font = ("Arial Bond", 15))
  boton2 = Button(ventana, text = "Salir", command = Salir2, font = ("Arial Bond", 15))
  boton1.place(x = 0, y = 150)
  boton2.place(x = 0, y = 190)

  ventana.mainloop()

def Opcion2(event):
  global ventana2
  global ntexto1
  global ntexto2
  global ntexto3
  global ntexto4
  global ntexto5
  global ntexto6
  ventana2 = Tk()
  ventana2.title("Verificar pensión")
  main.destroy()
  ventana2.configure(background = "Skyblue")

  ventana2.geometry("300x300")

  nlinea1 = Label(ventana2, text = "Nombre", font = ("Arial Bond", 15))
  nlinea1.configure(background = "Skyblue")
  nlinea2 = Label(ventana2, text = "Edad", font = ("Arial Bond", 15))
  nlinea2.configure(background = "Skyblue")
  nlinea3 = Label(ventana2, text = "Sexo", font = ("Arial Bond", 15))
  nlinea3.configure(background = "Skyblue")
  nlinea4 = Label(ventana2, text = "Sueldo", font = ("Arial Bond", 15))
  nlinea4.configure(background = "Skyblue")
  nlinea5 = Label(ventana2, text = "AFP", font = ("Arial Bond", 15))
  nlinea5.configure(background = "Skyblue")
  nlinea6 = Label(ventana2, text = "Pensión deseada", font = ("Arial Bond", 15))
  nlinea6.configure(background = "Skyblue")
  ntexto1 = Entry(ventana2)
  ntexto2 = Entry(ventana2)
  ntexto3 = Entry(ventana2)
  ntexto4 = Entry(ventana2)
  ntexto5 = Entry(ventana2)
  ntexto6 = Entry(ventana2)

  nlinea1.grid(row=0)
  nlinea2.grid(row=1)
  nlinea3.grid(row=2)
  nlinea4.grid(row=3)
  nlinea5.grid(row=4)
  nlinea6.grid(row=5)

  ntexto1.grid(row=0, column=1)
  ntexto2.grid(row=1, column=1)
  ntexto3.grid(row=2, column=1)
  ntexto4.grid(row=3, column=1)
  ntexto5.grid(row=4, column=1)
  ntexto6.grid(row=5, column=1)

  boton1 = Button(ventana2, text = "Siguiente", command = Siguiente2, font = ("Arial Bond", 15))
  boton2 = Button(ventana2, text = "Salir", command = Salir3, font = ("Arial Bond", 15))
  boton1.place(x = 0, y = 180)
  boton2.place(x = 0, y = 220)

  ventana2.mainloop()

def Siguiente():
  ventana3 = Tk()
  ventana3.title("Resultado")
  ventana3.geometry("600x50")
  ventana3.configure(background = "Skyblue")

  c = Usuario(texto1.get(), int(texto2.get()), texto3.get(), int(texto4.get()), texto5.get())
  Funcion1 = Label(ventana3, text = "La pensión de " + texto1.get() + " será de: " + str(c.ObtenerPension()) + " pesos", font = ("Arial Bond", 15))
  Funcion1.configure(background = "Skyblue")
  Funcion1.pack()

  ventana3.mainloop()    

def Siguiente2():
  ventana4 = Tk()
  ventana4.title("Resultado")
  ventana4.geometry("600x50")
  ventana4.configure(background = "Skyblue")

  d = Usuario(ntexto1.get(),int(ntexto2.get()), ntexto3.get(), int(ntexto4.get()), ntexto5.get())
  Funcion2 = Label(ventana4, text = str(d.VerificarPension(int(ntexto6.get()))), font = ("Arial Bond", 15))
  Funcion2.configure(background = "Skyblue")
  Funcion2.pack()

def Salir(event):
    main.destroy()       

def Salir2():
    ventana.destroy()

def Salir3():
    ventana2.destroy()

principal()
