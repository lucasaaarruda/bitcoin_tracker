from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from cores import *

# Janela Principal ---------------------------------------------------------------------

janela = Tk()
janela.title('Bitcoin Preço')
janela.geometry('320x350')
janela.configure(bg=fundo)

# Frames da Janela ---------------------------------------------------------------------

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=branco, pady=0, padx=0, relief='flat',)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0, relief='flat',)
frame_baixo.grid(row=2, column=0, sticky=NW)

# Configurando o frame cima ---------------------------------------------------------------------

imagem = Image.open('images/bit1.png')
imagem = imagem.resize((40, 40), Image.Resampling.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon1 = Label(frame_cima, image=imagem, compound=LEFT, bg=branco, relief=FLAT)
l_icon1.place(x=6, y=3)

l_nome = Label(frame_cima, text='Bitcoin Preço', bg=branco, fg=preto, relief=FLAT, anchor='center',
               font=('Arial 20'))
l_nome.place(x=50, y=5)

# Configurando o frame baixo ---------------------------------------------------------------------

l_dollar = Label(frame_baixo, text='', bg=fundo, fg=branco, relief=FLAT, anchor='center',
               font=('Arial 20'))
l_dollar.place(x=23, y=50)

l_reais = Label(frame_baixo, text='', bg=fundo, fg=branco, relief=FLAT, anchor='center',
               font=('Arial 14'))
l_reais.place(x=23, y=130)

l_euro = Label(frame_baixo, text='', bg=fundo, fg=branco, relief=FLAT, anchor='center',
               font=('Arial 14'))
l_euro.place(x=23, y=160)

l_libra = Label(frame_baixo, text='', bg=fundo, fg=branco, relief=FLAT, anchor='center',
               font=('Arial 14'))
l_libra.place(x=23, y=190)