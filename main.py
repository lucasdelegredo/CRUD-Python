from asyncio import windows_events
from tkinter import *
from turtle import left
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
#Message Box
from tkinter import messagebox
#Views
from view import *


#COLORS
co0 = "#0F0F0F" #preto
co1 = "#CDCDCD" #branco
co2 = "#3D6AC7"#bg2  blue
co3 = "#171717"#letra
co4 = "#FF4A26"# - profit
co5 = "#3535D5"#azul
co6 = "#DF2121"#vermelho
co7 = "#0D9100"# +verde
co8 = "#053600"# ++verde
co9 = "#001B52"# blue bg
# ####################

#window 
window = Tk()
window.title("Gerencimento de Equipamentos")
window.geometry('1024x768')
window.configure(background=co9)
window.resizable(width=TRUE,height=TRUE)
###################################################################

#window layout
frame_top = Frame(window, width=310,height=50,bg=co2,relief='flat')
frame_top.grid(row=0,column=0)

frame_bot = Frame(window, width=310,height=403,bg=co1,relief='flat')
frame_bot.grid(row=1,column=0,sticky=NSEW,padx=0,pady=1)

frame_right = Frame(window, width=588,height=403,bg=co1,relief='flat')
frame_right.grid(row=0,column=1,rowspan=2,padx=1,pady=0,sticky=NSEW)
###################################################################

#Label Top
app_name = Label(frame_top,text="Controle de Ativos",anchor=NW, font=('Ivy 13 bold'),bg=co2, fg=co1,relief='flat')
app_name.place(x=10,y=10)
###################################################################

#função inserir
def insert():
    ativo = e_ativo.get()
    tipo = e_tipo.get()
    marca = e_marca.get()
    modelo = e_modelo.get()
    dtafabr = e_dtafabr.get()
    valor = e_valor.get()
    cc = e_cc.get()
    area = e_area.get()
    obs = e_obs.get()

    lista = [ativo,tipo,marca,modelo,dtafabr,valor,cc,area,obs]

    if ativo=="":
        messagebox.showerror('Erro','A TAG do Ativo não pode ser vazio')
    else:
        insert_info(lista)
        messagebox.showinfo('Sucesso!',"Informações inseridas com sucesso!")
        #limpar campos
        e_ativo.delete(0,'end')
        e_tipo.delete(0,'end')
        e_marca.delete(0,'end')
        e_modelo.delete(0,'end')
        e_dtafabr.delete(0,'end')
        e_valor.delete(0,'end')
        e_cc.delete(0,'end')
        e_area.delete(0,'end')
        e_obs.delete(0,'end')
    
    for widget in frame_right.winfo_children():
        widget.destroy()
    
    mostrar()

def deletar():
    ativo = e_ativo.get()
    lista = [ativo]
    if ativo=="":
        messagebox.showerror('Erro','A TAG do Ativo não pode ser vazio para deletar')
    else:
        delete_info(lista)
        messagebox.showinfo('Sucesso!',"Informações apagadas com sucesso!")
        #limpar campos
        e_ativo.delete(0,'end')
    
    for widget in frame_right.winfo_children():
        widget.destroy()
    
    mostrar()
#Label_Bot

#ATIVO
label_ativo = Label(frame_bot,text="Ativo: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_ativo.place(x=10, y=20)

e_ativo = Entry(frame_bot,relief='solid',width=45,justify='left')
e_ativo.place(x=10,y=40)

#TIPO
label_tipo = Label(frame_bot,text="Tipo: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_tipo.place(x=10, y=60)

e_tipo = Entry(frame_bot,relief='solid',width=45,justify='left')
e_tipo.place(x=10,y=80) 

#MARCA
label_marca = Label(frame_bot,text="Marca: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_marca.place(x=10, y=100)

e_marca = Entry(frame_bot,relief='solid',width=20,justify='left')
e_marca.place(x=10,y=120) 

#MODELO
label_modelo = Label(frame_bot,text="Modelo: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_modelo.place(x=150, y=100)

e_modelo = Entry(frame_bot,relief='solid',width=20,justify='left')
e_modelo.place(x=150,y=120) 

#DTA_FABRIC
label_dtafabr = Label(frame_bot,text="Data Fabricação: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_dtafabr.place(x=10, y=140)

e_dtafabr = DateEntry(frame_bot,relief='solid',width=12,backgound='darkblue',foreground='white',borderwidth=2,justify='left')
e_dtafabr.place(x=10,y=160) 

#VALOR
label_valor = Label(frame_bot,text="Valor: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_valor.place(x=10, y=180)

e_valor = Entry(frame_bot,relief='solid',width=45,justify='left')
e_valor.place(x=10,y=200)

#CC
label_cc = Label(frame_bot,text="CC: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_cc.place(x=10, y=220)

e_cc = Entry(frame_bot,relief='solid',width=45,justify='left')
e_cc.place(x=10,y=240) 

#AREA
label_area = Label(frame_bot,text="Area: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_area.place(x=10, y=260)

e_area = Entry(frame_bot,relief='solid',width=45,justify='left')
e_area.place(x=10,y=280) 

#OBS
label_obs = Label(frame_bot,text="Obs: ",anchor=NW,font=('Ivy 12 bold'),bg=co1,fg=co0,relief='flat')
label_obs.place(x=10, y=300)

e_obs = Entry(frame_bot,relief='solid',width=45,justify='left')
e_obs.place(x=10,y=320) 

#BUTTONS ---------------------------------

#INSERT
b_insert = Button(frame_bot,command=insert,text='Cadastrar',width=10,font=('Ivy 10 bold'),bg=co7,fg=co1,relief='raised',overrelief='ridge')
b_insert.place(x=10,y=360)

#UPDATE
b_update = Button(frame_bot,text='Update',width=10,font=('Ivy 10 bold'),bg=co5,fg=co1,relief='raised',overrelief='ridge')
b_update.place(x=110,y=360)

#DELETE
b_delete = Button(frame_bot,command=deletar,text='Delete',width=10,font=('Ivy 10 bold'),bg=co6,fg=co1,relief='raised',overrelief='ridge')
b_delete.place(x=210,y=360)

#------------------------------------------------------------------

def mostrar():
        
    lista = view_info()

    # lista para cabecario
    tabela_head = ['Ativo','Tipo',  'Marca','Modelo', 'Data Fabricação', 'Valor','CC','Area','Obs']


    # criando a tabela
    tree = ttk.Treeview(frame_right, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_right, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_right, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_right.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100,120,140]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

#função para mostrar
mostrar()

window.mainloop()