import tkinter as tk


def iniciarJanela():

    pass


mw = tk.Tk()

mw.option_add("*Button.Background", "black")
mw.option_add("*Button.Foreground", "#1B5E20")

mw.title('Sistema de Gerenciamento')
mw.geometry("1024x768")
mw.resizable(0, 0)

back = tk.Frame(master=mw, bg='#f1f1f1')
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)
go = tk.Button(
    master=back,  text='Inicio', command=iniciarJanela,  height=5, width=25, padx=50, pady=10, )
go.pack()


close = tk.Button(
    master=back, text='Sair', command=mw.destroy, height=10, width=25)

close.pack()
info = tk.Label(master=back, text='Desenvolvido Por João',
                bg='#f1f1f1', fg='#212121')
info.pack()
mw.mainloop()
