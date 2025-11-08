import tkinter as tk
from tkinter import messagebox

empregados={}

def gui():
   root=tk.Tk()
   root.geometry("500x500")
   root.wm_resizable(False,False)

   name_label=tk.Label(root,text="Nome :")
   name_label.place(x=30,y=30)
   name_entry=tk.Entry(root,width=60)
   name_entry.place(x=90,y=30)

   gender_label = tk.Label(root, text="Género :")
   gender_label.place(x=30, y=100)
   gender_entry = tk.Entry(root, width=60)
   gender_entry.place(x=90, y=100)

   idade_label = tk.Label(root, text="Idade :")
   idade_label.place(x=30, y=170)
   idade_entry = tk.Entry(root, width=60)
   idade_entry.place(x=90, y=170)

   nif_label = tk.Label(root, text="NIF :")
   nif_label.place(x=30, y=240)
   nif_entry = tk.Entry(root, width=60)
   nif_entry.place(x=90, y=240)

   registar_button=tk.Button(root,width=15,height=3,text="Registar",command=lambda:registar(name_entry.get(),gender_entry.get(),idade_entry.get(),nif_entry.get()))
   registar_button.place(x=50,y=310)

   consultar_button = tk.Button(root, width=15, height=3, text="Consultar",command=lambda:consultar(nif_entry.get()))
   consultar_button.place(x=300, y=310)

   root.mainloop()


def registar(nome,genero,idade,nif):
    try:
        nif=int(nif)
        idade=int(idade)

        if nif in empregados:
            messagebox.showerror("Coiso", "NIF já registado")
        else:
            empregados[int(nif)] = [nome, int(idade), genero]
            messagebox.showinfo("Coiso", "Empregado registado")


    except:
        messagebox.showerror("Coiso", "NIF ou Idade inválido")

def consultar(nif):
    try:
        nif = int(nif)

        if nif in empregados:
            messagebox.showinfo("Coiso",
                                f"Nome:{empregados[nif][0]}\nIdade:{empregados[nif][1]}\nGénero:{empregados[nif][2]}\n")
        else:
            messagebox.showerror("Coiso", "NIF não existente")

    except:
        messagebox.showerror("Coiso", "NIF inválido")

gui()
