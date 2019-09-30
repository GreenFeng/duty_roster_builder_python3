import tkinter as tk
root = tk.Tk('order')
welcome = tk.Label(root,text="welcome to order system")
welcome.pack(side=tk.TOP)
welcome.config(fg='green')

bey = tk.Label(root,text="if you'd like to leve")
bey.config(fg='#f00101',bg='#20f0f0')
bey.pack(expand=tk.YES,fill=tk.X)

change_bg = tk.Button(root,text='chang color',command=color_change)
change_bg.pack()

root.mainloop()

def color_change():
	bey.config(bg='white')