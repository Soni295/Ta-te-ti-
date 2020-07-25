from tkinter import Button, Tk, Frame

from tkinter import font as tkFont

raiz= Tk()
frame=Frame(raiz)
frame.pack()

class Computer:
  def __init__(self):
    self.btn=Button(frame, text="IA",  width=3, heigh=1, )
    self.btn.grid(row=3, column=3)  

class Boton:

  def __init__(self, row, column,indice):
    self.indice=indice
    self.valor=True
    self.btn= Button(frame, text="",  width=3, heigh=1, command= lambda:turno(self))
    self.btn["font"]=tkFont.Font(family='Helvetica', size=30, weight='bold')    
    self.btn.grid(row=row, column=column)
    self.texto=""

  def marcar(self,valor):
    if(valor==True):
      self.btn.config(disabledforeground="#F50743")
      self.texto="X"
    else:
      self.btn.config(disabledforeground="#07EDFD")
      self.texto="O"    
    self.btn.config(text=self.texto)
    self.bloquear()

  def bloquear(self):
    self.btn["state"]="disabled"

  def reset(self):
    self.btn["state"]="active"
    self.btn.config(text="")

class Tabla():
  
  def __init__(self):
    self.__tablero = ["" for i in range(9)]

    self.botones=[
      Boton( 0, 0, 0), 
      Boton( 0, 1, 1), 
      Boton( 0, 2, 2), 
      Boton( 1, 0, 3), 
      Boton( 1, 1, 4), 
      Boton( 1, 2, 5), 
      Boton( 2, 0, 6), 
      Boton( 2, 1, 7), 
      Boton( 2, 2, 8)
    ]  
    """
    0 1 2
    3 4 5
    6 7 8
    """
    self.patrones_ganadores=[
      [0, 3, 6], [1, 4, 7],
      [2, 5, 8], [0, 1, 2],
      [3, 4, 5], [6, 7, 8],
      [0, 4, 8], [2, 4, 6]
    ]

    self.marca=True

  def mostrar(self):
    print(self.__tablero[0])

  def bloquear(self):
    for btn in self.botones:
      btn.bloquear()
  
  def nuevoJuego(self):
    for btn in self.botones:
      btn.reset()
    tablero.reset()

  def enviarMarca(self):
    self.enviar=self.marca
    
    if(self.marca == True):
      self.marca=False
    else:
      self.marca=True
    return self.enviar

  def reset(self):
    for i in range(9):
      self.__tablero[i]=""

  def marcar(self,casilla,signo):
    self.__tablero[casilla]=signo
    self.quien_gano()

  def quien_gano(self):    
    for i in self.patrones_ganadores:
      print(i[0])
      if(self.__tablero[i[0]] ==self.__tablero[i[1]] ==self.__tablero[i[2]]!= ""):        
        finalDelJuego()
        break
    
def turno(obj):  
  obj.marcar(tablero.enviarMarca())
  tablero.marcar(obj.indice , obj.texto)


def finalDelJuego():
  print("Bloquear Todos los botones")
  tablero.bloquear()
  #nueva_partida()

def nueva_partida():
  tablero.nuevoJuego()



tablero = Tabla()

raiz.mainloop()