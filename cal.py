from tkinter import*
from tkinter import messagebox


ventana = Tk()
ventana.title("Calculadora 1")
ventana.iconbitmap("Calculadora\operadores.ico")
ventana.resizable(0,0)
ventana.configure(background="white")
ventana.geometry("445x300")
ventana.geometry("+10+10")
ventana.config(cursor="plus")
Lbl_nom= Label(ventana, fg="black", bg="white", font=("Arial", 10))
Lbl_nom.place(x=330, y=270)


def suma():
    try:
        num1 = Ent_val1.get()
        num2 = Ent_val2.get()

        if num1 == "" or num2 == "":
            Lbl_Resul ["text"] = ""
            messagebox.showinfo("Faltan valores")
        else:
            resul = int(num1) + int(num2)
            Lbl_Resul["text"] = resul
    except:
        messagebox.showerror("Los valores ingresados no son validos")

def resta():
    try:
        num1 = Ent_val1.get()
        num2 = Ent_val2.get()

        if num1 == "" or num2 == "":
            Lbl_Resul ["text"] = ""
            messagebox.showinfo("Faltan valores")
        else:
            resul = int(num1) - int(num2)
            Lbl_Resul["text"] = resul
    except:
        messagebox.showerror("Los valores ingresados no son validos")
        
def multi():
    try:
        num1 = Ent_val1.get()
        num2 = Ent_val2.get()

        if num1 == "" or num2 == "":
            Lbl_Resul ["text"] = ""
            messagebox.showinfo("Faltan valores")
        else:
            resul = float(num1) * float(num2)
            Lbl_Resul["text"] = resul
    except:
        messagebox.showerror("Los valores ingresados no son validos")

def div():
    try:
        num1 = Ent_val1.get()
        num2 = Ent_val2.get()

        if num1 == "" or num2 == "":
            Lbl_Resul ["text"] = ""
            messagebox.showinfo("Faltan valores")
        else:
            resul = float(num1) / float(num2)
            Lbl_Resul["text"] = resul
    except:
        messagebox.showerror("Los valores ingresados no son validos")

operaciones = LabelFrame(ventana, text="operaciones", width=428, height=102, background="white", fg="black",  font=("Arial", 10))
operaciones.place(x=10, y=20)

Lbl_num1 = Label(ventana, text="Numero 1", fg="black", bg="white", font=("Arial", 10))
Lbl_num1.place(x=30, y=40)

Lbl_num2 = Lbl_num1 = Label(ventana, text="Numero 2", fg="black", bg="white", font=("Arial", 10))
Lbl_num2.place(x=190, y=40)

Lbl_Resul = Lbl_num1 = Label(ventana, text="Resultado", fg="black", bg="white", font=("Arial", 10))
Lbl_Resul.place(x=370, y=70)

Ent_val1 = Entry(ventana,fg="black", font=("Arial", 10), width=8, justify=RIGHT)
Ent_val1.place(x=30, y=70)
Ent_val1.insert(0, "7")

Lbl_Signo = Label(ventana, text="(+ - x ÷)", fg="black", bg="white", font=("Arial", 10))
Lbl_Signo.place(x=110, y=70)

Ent_val2 = Entry(ventana, fg="black", font=("Arial", 10), width=8, justify=RIGHT)
Ent_val2.place(x=190, y=70)
Ent_val2.insert(0, "2")

Lbl_igual = Label(ventana, text="=", fg="black", bg="white", font=("Arial", 10))
Lbl_igual.place(x=290, y=70)

Lbl_res = Label(ventana, text="", fg="black", bg="white", font=("Arial", 10))
Lbl_res.place(x=340, y=70)

op_arit = LabelFrame(ventana, text="Operadores Aritmeticos", width=428, height=108, background="black", fg="black", font=("Arial",10))
op_arit.place(x=10, y=160)

boton_sum = Button(ventana, text="+", width=10, height=4, background="white", fg="black", command=suma)
boton_sum.place(x=25, y=180)

boton_res = Button(ventana, text="-", width=10, height=4, background="white", fg="black", command=resta)
boton_res.place(x=130, y=180)

boton_multi = Button(ventana, text="x", width=10, height=4, background="white", fg="black", command= multi)
boton_multi.place(x=235, y=180)

boton_div = Button(ventana, text="÷", width=10, height=4, background="white", fg="black", command=div)
boton_div.place(x=340, y=180)

ventana.mainloop()