from tkinter import*
ventana = Tk()
ventana.title("Calculadora 2.0")

Ent_text = Entry(ventana, font=("Arial 10"))
Ent_text.grid(row= 0, column = 0, columnspan = 5, padx = 5, pady = 5)

i = 0

def click (valor):
    global i
    Ent_text.insert(i, valor)
    i+=1
    
def raiz ():
    EC1 = Ent_text.get()
    Res1 = eval(EC1)
    Res2 = Res1** (0.5)
    Ent_text.delete(0, END) 
    Ent_text.insert(0, Res2)
    i = 0
    
def porciento ():
    EC1 = Ent_text.get()
    Res1 = eval(EC1)
    Res2 = Res1**(0.01)
    Ent_text.delete(0, END) 
    Ent_text.insert(0, Res2)
    i = 0
    
def uno_sobre_x ():
    EC1 = Ent_text.get()
    Res1 = eval(EC1)
    Res2 = 1/Res1
    Ent_text.delete(0, END) 
    Ent_text.insert(0, Res2)
    i = 0

def limpiar_pantalla ():
    Ent_text.delete(0, END)
    i = 0
    
def op ():
    EC = Ent_text.get()
    Res = eval(EC)
    Ent_text.delete(0, END) 
    Ent_text.insert(0, Res)
    i = 0
      
click1 = Button(ventana, text = "1", width = 5, height = 2,command = lambda: click(1))
click2 = Button(ventana, text = "2", width = 5, height = 2,command = lambda: click(2))
click3 = Button(ventana, text = "3", width = 5, height = 2,command = lambda: click(3))
click4 = Button(ventana, text = "4", width = 5, height = 2,command = lambda: click(4))
click5 = Button(ventana, text = "5", width = 5, height = 2,command = lambda: click(5))
click6 = Button(ventana, text = "6", width = 5, height = 2,command = lambda: click(6))
click7 = Button(ventana, text = "7", width = 5, height = 2,command = lambda: click(7))
click8 = Button(ventana, text = "8", width = 5, height = 2,command = lambda: click(8))
click9 = Button(ventana, text = "9", width = 5, height = 2,command = lambda: click(9))
click0 = Button(ventana, text = "0", width = 16,height = 2,command = lambda: click(0))

a = Button(ventana, text = "<--", width = 5, height = 2,command = lambda: click("a"))
MC = Button(ventana, text = "MC" , width = 5, height = 2,command = lambda: limpiar_pantalla())
c = Button(ventana, text = "C"  , width = 5, height = 2,command = lambda: limpiar_pantalla)
d = Button(ventana, text = "±"  , width = 5, height = 2,command = lambda: click("d"))
e = Button(ventana, text = "√"  , width = 5, height = 2,command = lambda: raiz())

MR = Button(ventana, text = "MR" , width = 5, height = 2,command = lambda: MR())
M_mas = Button(ventana, text = "M+" , width = 5, height = 2,command = lambda: M_mas())
porcentaje = Button(ventana, text = "%"  , width = 5, height = 2,command = lambda: porciento())
unosobrex = Button(ventana, text = "1/x", width = 5, height = 2,command = lambda: uno_sobre_x())
sqr = Button(ventana, text = "sqr", width = 5, height = 2,command = lambda: click("sqr"))
MS = Button(ventana, text = "MS" , width = 5, height = 2,command = lambda: click(")"))
decimal = Button(ventana, text = "." , width = 5, height = 2,command = lambda: click("."))
borrar1 = Button(ventana, text = "CE", width = 5, height = 2,command = lambda: limpiar_pantalla())

suma  = Button(ventana, text = "+", width = 5, height = 2,command = lambda: click("+"))
resta = Button(ventana, text = "-", width = 5, height = 2,command = lambda: click("-"))
multi = Button(ventana, text = "*", width = 5, height = 2,command = lambda: click("*"))
divi  = Button(ventana, text = "÷", width = 5, height = 2,command = lambda: click("/"))
igual = Button(ventana, text = "=", width = 5, height = 6,command = lambda: op())

MC.grid(         row=1, column=0, padx=5, pady=5)
MR.grid(row=1, column=1, padx=5, pady=5) 
MS.grid(row=1, column=2, padx=5, pady=5) 
M_mas.grid(       row=1, column=3, padx=5, pady=5)
sqr.grid(        row=1, column=4, padx=5, pady=5)

a.grid(row=2, column=0, padx=5, pady=5)
borrar1.grid(row=2, column=1, padx=5, pady=5) 
c.grid(row=2, column=2, padx=5, pady=5)
d.grid(row=2, column=3, padx=5, pady=5)
e.grid(row=2, column=4, padx=5, pady=5)

click1.grid(row=5, column=0, padx=5, pady=5)
click2.grid(row=5, column=1, padx=5, pady=5)
click3.grid(row=5, column=2, padx=5, pady=5)
click4.grid(row=4, column=0, padx=5, pady=5)
click5.grid(row=4, column=1, padx=5, pady=5)
click6.grid(row=4, column=2, padx=5, pady=5)
click7.grid(row=3, column=0, padx=5, pady=5)
click8.grid(row=3, column=1, padx=5, pady=5)
click9.grid(row=3, column=2, padx=5, pady=5)
click0.grid( row=6, column=0, columnspan=2, padx=5, pady=5)

resta.grid( row=5, column=3, padx=5, pady=5)
igual.grid( row=5, column=4, padx=5, rowspan=5, pady=5)
decimal.grid(row=6, column=2, padx=5, pady=5)
suma.grid(   row=6, column=3, padx=5, pady=5)
divi.grid(row=3, column=3, padx=5, pady=5)
porcentaje.grid(row=3, column=4, padx=5, pady=5)
multi.grid( row=4, column=3, padx=5, pady=5)
unosobrex.grid(row=4, column=4, padx=5, pady=5)




ventana.mainloop()

