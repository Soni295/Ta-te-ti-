from tkinter import *

from tkinter import font as tkFont

raiz= Tk()
frame=Frame(raiz)
frame.pack()

class Boton:
  def __init__(self, row, column,indice):
    self.indice=indice
    self.text=""
    self.valor="X"
    tamano=tkFont.Font(family='Helvetica', size=30, weight='bold')
    self.btn= Button(frame, text=self.text,  width=3, heigh=1, command= lambda:turno(self))
    self.btn["font"]=tamano
    self.btn.grid(row=row, column=column)    
 
  def bloquear(self):    
    self.btn["state"]="disabled"

  def reset(self):
    self.btn["state"]="active"
    self.btn.config(text="")

class Tabla():
  def __init__(self):
    self.__tablero={
      1:"",2:"",3:"",
      4:"",5:"",6:"",
      7:"",8:"",9:""
    }
    
    self.patrones_ganadores=[
      [1, 4, 7], [2, 5, 8],
      [3, 6, 9], [1, 2, 3],
      [4, 5, 6], [7, 8, 9],
      [1, 5, 9], [3, 5, 7]
    ]
    self.marca="X"

  def enviarMarca(self):
    self.enviar=self.marca
    
    if(self.enviar =="X"):
      self.marca="O"
    else:
      self.marca="X"
    return self.enviar

  def reset(self):
    for i in self.__tablero:
      self.__tablero[i]=""

  def marcar(self,casilla,signo):
    self.__tablero[casilla]=signo
    self.quien_gano()

  def mostrar(self):
    print(self.__tablero)

  def quien_gano(self):    
    for i in self.patrones_ganadores:
      if(self.__tablero[i[0]] ==self.__tablero[i[1]] ==self.__tablero[i[2]]!= ""):        
        finalDelJuego()
        break
    print(self.__tablero)
  
class Game():
  def __init__(self):
    self.botones=[
      Boton( 0, 0, 1), 
      Boton( 0, 1, 2), 
      Boton( 0, 2, 3), 
      Boton( 1, 0, 4), 
      Boton( 1, 1, 5), 
      Boton( 1, 2, 6), 
      Boton( 2, 0, 7), 
      Boton( 2, 1, 8), 
      Boton( 2, 2, 9)]    

  def bloquear(self):
    for btn in self.botones:
      btn.bloquear()
  
  def nuevoJuego(self):
    for btn in self.botones:
      btn.reset()
    tablero.reset()

game=Game()


def finalDelJuego():
  print("Bloquear Todos los botones")
  nueva_partida()

def nueva_partida():
  game.bloquear()
  game.nuevoJuego()

def turno(obj):  
  obj.text=tablero.enviarMarca()
  obj.btn.config(text=obj.text)
  obj.btn["state"]="disabled"
  tablero.marcar(obj.indice,obj.text)

tablero= Tabla()

raiz.mainloop()