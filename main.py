from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

root.configure(background='#282828')

entrada = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#A7A28F', font=('futura', 25, 'bold'),
                justify=CENTER)
entrada.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2,
)


# Funções Operadores
def botao_divisao():
    return
def botao_click():
    return
def botao_multiplica():
    return
def botao_soma():
    return
def botao_subtracao():
    return
def botao_limpar():
    return
def botao_igual():
    return


divide = Button(
    root,
    text='÷',
    padx=41,
    pady=20,
    command=botao_divisao,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
divide.grid(row=0, column=4)

# Primeira fileira

um = Button(
    root,
    text='1',
    padx=41,
    pady=20,
    command=lambda: botao_click(1),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(
    root,
    text='2',
    padx=41,
    pady=20,
    command=lambda: botao_click(2),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(
    root,
    text='3',
    padx=41,
    pady=20,
    command=lambda: botao_click(3),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
tres.grid(row=1, column=3)

multiplica = Button(
    root,
    text='×',
    padx=42,
    pady=20,
    command=botao_multiplica(),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
multiplica.grid(row=1, column=4)

# Segunda Fileira
quatro = Button(
    root,
    text='4',
    padx=41,
    pady=20,
    command=lambda: botao_click(4),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(
    root,
    text='5',
    padx=41,
    pady=20,
    command=lambda: botao_click(5),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

seis = Button(
    root,
    text='6',
    padx=41,
    pady=20,
    command=lambda: botao_click(6),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)

soma = Button(
    root,
    text='+',
    padx=41,
    pady=20,
    command=botao_soma,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
soma.grid(row=2, column=4)

# Terceira Fileira
sete = Button(
    root,
    text='7',
    padx=41,
    pady=20,
    command=lambda: botao_click(7),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
sete.grid(row=3, column=1)

oito = Button(
    root,
    text='8',
    padx=41,
    pady=20,
    command=lambda: botao_click(8),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
oito.grid(row=3, column=2)

nove = Button(
    root,
    text='9',
    padx=41,
    pady=20,
    command=lambda: botao_click(9),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
nove.grid(row=3, column=3)

subtracao = Button(
    root,
    text='-',
    padx=42.5,
    pady=20,
    command=botao_subtracao,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
subtracao.grid(row=3, column=4)

# Quarta Fileira
zero = Button(
    root,
    text='0',
    padx=92.5,
    pady=20,
    command=lambda: botao_click(0),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)

limpar = Button(
    root,
    text='C',
    padx=40,
    pady=20,
    command=botao_limpar,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
limpar.grid(row=4, column=3)

igual = Button(
    root,
    text='=',
    padx=41.5,
    pady=20,
    command=botao_igual,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
igual.grid(row=4, column=4)

root.mainloop()
