import tkinter as tk

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

   registar_button=tk.Button(root,width=15,height=3,text="Registar",command=registar)
   registar_button.place(x=50,y=310)

   root.mainloop()


def registar(name_entry,idade_entry,gender_entry,nif_entry):
    nome = name_entry.get
    idade = idade_entry.get
    genero = gender_entry.get
    nif = nif_entry.get

    empregados[nif]=[nome,idade,genero]
    print(empregados)



gui()
