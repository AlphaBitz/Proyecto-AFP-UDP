class Usuario:
  def __init__(self, nombre, edad, sexo, sueldo, AFP):
    self.nombre = nombre 
    self.edad = edad 
    self.sexo = sexo  
    self.sueldo=sueldo 
    self.AFP = AFP 
    
  def Obtenercapital (self):   #Calculo de la Capital, Con la comision base del 10% mas la respectiva de cada AFP, ademas de la rentabilidad de 5%
      if (self.AFP=="Capital" or self.AFP=="capital"):
          capital=self.sueldo*0.1144*1.05
          return (capital)
      if (self.AFP=="Cuprum" or self.AFP=="cuprum"):
          capital=self.sueldo*0.1144*1.05
          return (capital)
      if (self.AFP == "Habitat" or self.AFP == "habitat"):
          capital=self.sueldo*0.1127*1.05
          return (capital)
      if (self.AFP == "Modelo" or self.AFP == "modelo"):
          capital=self.sueldo*0.1077*1.05
          return (capital)
      if (self.AFP == "Planvital" or self.AFP == "planvital"):
          capital=self.sueldo*0.1116*1.05
          return (capital)
      if (self.AFP == "Provida" or self.AFP == "provida"):
          capital=self.sueldo*0.1145*1.05
          return (capital)
      print ("AFP invalida")
     
  def ObtenerPension(self): #Obtencion de la pension, con la esperanza de vida del y la jubilacion de cada sexo respectivamente. (Opcion 1)
     C=self.Obtenercapital()
     if (self.sexo=="Hombre" or self.sexo=="hombre"):
         V1=C*(65-self.edad)
         V2= V1/((85-65))
         return (V2)
     if (self.sexo=="Mujer" or self.sexo=="mujer"):
         V1=C*(60-self.edad)
         V2=V1/((90-60))
         return (V2)

  def VerificarPension(self,estimado): #obtencion del monto restante necesario para llegar al monto objetivo. (Opcion 2)
     pension=self.ObtenerPension()
     dif=estimado-pension
     if dif<0:
       print("La jubilación es mayor que la proyección:" , pension)
       return
     if self.sexo=="Hombre":
       N1=dif*20*12
       N2=(N1/(65-self.edad))/12
     if self.sexo=="Mujer":
       N1=dif*30*12
       N2=(N1/(60-self.edad))/12
     N3=N2*0.97 #Rentabilidad del 3% APV
     print (N3)
     return

b=Usuario("Juan",20,"Hombre",10000,"Capital")
print (b.ObtenerPension())
b.VerificarPension(300000)

