from tkinter import *
raiz= Tk()
frame=Frame(raiz)
frame.pack()

class Tabla():
  def __init__(self):
    self.__tablero={
      1:" ",2:" ",3:" ",
      4:" ",5:" ",6:" ",
      7:" ",8:" ",9:" ",
    }
    
    self.patrones_ganadores=[
      [1, 4, 7], [2, 5, 8],
      [3, 6, 9], [1, 2, 3],
      [4, 5, 6], [7, 8, 9],
      [1, 5, 9], [3, 5, 7]
    ]
  def marcar(self,casilla,signo):
    self.__tablero[casilla]=signo
    self.quien_gano()

  def mostrar(self):
    print(self.__tablero)

  def quien_gano(self):
    print(self)



tablero= Tabla()

tablero.marcar(2,"X")

tablero.mostrar()


raiz.mainloop()