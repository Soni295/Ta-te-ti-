from tkinter import *
from tkinter import font as tkFont

raiz= Tk()

frame=Frame(raiz)
frame.pack()

class Boton:
  def __init__(self, row, column,indice,func):
    self.indice=indice
    self.text=" "
    tamano=tkFont.Font(family='Helvetica', size=30, weight='bold')
    self.btn= Button(frame, text=self.text,  width=3, heigh=1, command= lambda:func(self))
    self.btn["font"]=tamano
    self.btn.grid(row=row, column=column)
    
 
  def restart(self):
    self.btn.config(text=" ")
    
    self.btn["state"]="enable"
  
  def asignar(self,valor):
    self.text=valor
    self.btn.config(text=self.text)
    self.btn["state"]="disabled"

class Juego():
  def __init__(self):
    
    self.turno=True
    
    self.posicion={
      1:"", 2:"", 3:"",
      4:"", 5:"", 6:"",
      7:"", 8:"", 9:""
    }

    bonton1=Boton( 0, 0, 1, self.seleccion)
    bonton2=Boton( 0, 1, 2, self.seleccion)
    bonton3=Boton( 0, 2, 3, self.seleccion)
    bonton4=Boton( 1, 0, 4, self.seleccion)
    bonton5=Boton( 1, 1, 5, self.seleccion)
    bonton6=Boton( 1, 2, 6, self.seleccion)
    bonton7=Boton( 2, 0, 7, self.seleccion)
    bonton8=Boton( 2, 1, 8, self.seleccion)
    bonton9=Boton( 2, 2, 9, self.seleccion)

  def jugada(self):
    
    if(self.turno):
      self.turno=False
      return "X"
    
    self.turno=True
    return "O"

  def seleccion(self,btn):
    quien_va=self.jugada()
    self.posicion[btn.indice]= quien_va
    btn.asignar(quien_va)


def eleccion():
  pass


class Marcador:
  def __init__(self, row, column):
    self.partidas=0
    self.ganoX=0
    self.ganoO=0
    self.label=Label(frame, font=(15))
    self.label.grid(row=row, column=column)
    self.contador()
  
  def contador(self):
    self.texto = "Partidas jugadas: "+str(self.partidas)
    self.texto += "\nGanadas X: "+str(self.ganoX)
    self.texto += "\nGanadas O: "+str(self.ganoO)
    print(self.texto)
    self.label.config(text=self.texto)



miLabel=Marcador(0,3)




def tipoDeJuego(jugador):
  return jugador



Juego()



raiz.mainloop()